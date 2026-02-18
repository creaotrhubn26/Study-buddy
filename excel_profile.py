#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

import pandas as pd


def infer_column_kind(series: pd.Series) -> str:
    if pd.api.types.is_numeric_dtype(series):
        return "numeric"
    if pd.api.types.is_datetime64_any_dtype(series):
        return "date"

    if series.dtype == "object":
        non_null = series.dropna()
        if non_null.empty:
            return "empty"
        parsed = pd.to_datetime(non_null, errors="coerce", utc=False)
        ratio = parsed.notna().mean()
        if ratio >= 0.8:
            return "date-like"
        return "text"

    return str(series.dtype)


def sheet_profile(df: pd.DataFrame, sheet_name: str, top_n: int = 5) -> dict:
    row_count, col_count = df.shape
    missing = df.isna().sum()
    missing_pct = (missing / row_count * 100).round(2) if row_count else missing

    kinds = {col: infer_column_kind(df[col]) for col in df.columns}

    numeric_cols = [c for c in df.columns if kinds[c] == "numeric"]
    date_cols = [c for c in df.columns if kinds[c] in {"date", "date-like"}]
    text_cols = [c for c in df.columns if kinds[c] == "text"]

    duplicate_rows = int(df.duplicated().sum()) if row_count else 0

    numeric_summary = {}
    if numeric_cols:
        desc = df[numeric_cols].describe().T
        numeric_summary = {
            col: {
                "count": float(desc.loc[col, "count"]),
                "mean": float(desc.loc[col, "mean"]),
                "std": float(desc.loc[col, "std"]) if pd.notna(desc.loc[col, "std"]) else None,
                "min": float(desc.loc[col, "min"]),
                "25%": float(desc.loc[col, "25%"]),
                "50%": float(desc.loc[col, "50%"]),
                "75%": float(desc.loc[col, "75%"]),
                "max": float(desc.loc[col, "max"]),
            }
            for col in numeric_cols
        }

    date_ranges = {}
    for col in date_cols:
        parsed = pd.to_datetime(df[col], errors="coerce", utc=False)
        valid = parsed.dropna()
        if not valid.empty:
            date_ranges[col] = {
                "min": str(valid.min()),
                "max": str(valid.max()),
                "valid_count": int(valid.shape[0]),
            }

    top_categories = {}
    for col in text_cols[:5]:
        vc = df[col].value_counts(dropna=True).head(top_n)
        if not vc.empty:
            top_categories[col] = {str(k): int(v) for k, v in vc.items()}

    candidate_id_columns = []
    if row_count:
        for col in df.columns:
            non_null = df[col].dropna()
            if non_null.empty:
                continue
            uniqueness_ratio = non_null.nunique() / len(non_null)
            if uniqueness_ratio >= 0.98:
                candidate_id_columns.append(col)

    return {
        "sheet": sheet_name,
        "rows": row_count,
        "columns": col_count,
        "column_names": list(df.columns),
        "column_kinds": kinds,
        "missing_values": {
            col: {"count": int(missing[col]), "pct": float(missing_pct[col]) if row_count else 0.0}
            for col in df.columns
            if int(missing[col]) > 0
        },
        "duplicate_rows": duplicate_rows,
        "candidate_id_columns": candidate_id_columns,
        "numeric_summary": numeric_summary,
        "date_ranges": date_ranges,
        "top_categories": top_categories,
        "preview": df.head(top_n).fillna("").to_dict(orient="records"),
    }


def print_profile(profile: dict) -> None:
    print(f"\n=== Sheet: {profile['sheet']} ===")
    print(f"Rows: {profile['rows']:,} | Columns: {profile['columns']}")
    print(f"Columns: {', '.join(profile['column_names'])}")

    print("\nColumn kinds:")
    for col, kind in profile["column_kinds"].items():
        print(f"- {col}: {kind}")

    print(f"\nDuplicate rows: {profile['duplicate_rows']:,}")

    if profile["candidate_id_columns"]:
        print(f"Candidate ID columns: {', '.join(profile['candidate_id_columns'])}")

    if profile["missing_values"]:
        print("\nMissing values:")
        for col, stats in profile["missing_values"].items():
            print(f"- {col}: {stats['count']:,} ({stats['pct']}%)")
    else:
        print("\nMissing values: none")

    if profile["date_ranges"]:
        print("\nDate ranges:")
        for col, stats in profile["date_ranges"].items():
            print(f"- {col}: {stats['min']} -> {stats['max']} (valid: {stats['valid_count']:,})")

    if profile["numeric_summary"]:
        print("\nNumeric summary (mean/min/max):")
        for col, stats in profile["numeric_summary"].items():
            print(f"- {col}: mean={stats['mean']:.4f}, min={stats['min']:.4f}, max={stats['max']:.4f}")

    if profile["top_categories"]:
        print("\nTop categories:")
        for col, values in profile["top_categories"].items():
            shown = ", ".join([f"{k} ({v})" for k, v in values.items()])
            print(f"- {col}: {shown}")

    print("\nPreview:")
    for row in profile["preview"]:
        print(row)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Profile Excel files and show important data quality/statistical insights."
    )
    parser.add_argument("file", help="Path to .xlsx file")
    parser.add_argument("--sheet", help="Profile only this sheet name", default=None)
    parser.add_argument("--top", type=int, default=5, help="Rows/categories to preview (default: 5)")
    parser.add_argument("--json-out", help="Optional path to save full profile JSON", default=None)
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    workbook = pd.ExcelFile(file_path)
    sheets = [args.sheet] if args.sheet else workbook.sheet_names

    profiles = []
    print(f"Workbook: {file_path}")
    print(f"Sheets found: {', '.join(workbook.sheet_names)}")

    for sheet in sheets:
        if sheet not in workbook.sheet_names:
            print(f"\nSkipping missing sheet: {sheet}")
            continue
        df = pd.read_excel(workbook, sheet_name=sheet)
        profile = sheet_profile(df, sheet_name=sheet, top_n=args.top)
        profiles.append(profile)
        print_profile(profile)

    if args.json_out:
        out_path = Path(args.json_out)
        out_path.write_text(json.dumps(profiles, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nSaved JSON profile: {out_path}")


if __name__ == "__main__":
    main()
