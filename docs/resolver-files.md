# Exam Resolver file workflow

Open **Universal Exam Resolver**, paste the brief and attach CSV/Excel files.
Then open **Create Excel, illustrations and PowerPoint**. All instructions and
generated explanations are in English.

1. **Create analysis plan** uses the configured text provider to propose a JSON
   plan from the complete supplied brief/documents, column names and a data preview.
   **Start from dataset template** works without an AI key. Review the proposed
   steps, units, assumptions, references and unresolved requirements. The JSON
   editor exposes the exact plan used for file generation.
2. **Build Excel and chart previews** executes that plan against complete source
   tables. Download the workbook with native editable charts. Source sheets and
   derived tables include linked formulas and computed cached results. Review
   the previews and measured findings. PNG previews are not Excel screenshots.
3. Generate each planned illustration explicitly. Review its prompt first.
   Each button sends one chargeable image request to OpenAI. Successful images
   survive reruns; failed or uncertain requests are never retried automatically.
   Original bytes are retained. Crop controls create a 16:9 edited version;
   before/after slides record the actual crop and source credit.
4. **Build PowerPoint and review pack** creates a native editable chart for each
   selected visualisation, with embedded workbook snapshots. It also includes
   title, agenda, executive summary, data/assumptions, supplied background,
   summary, source references and image editing evidence. Long chart explanations
   receive separate interpretation slides rather than overflowing the chart.
   Generation prompts
   and speaker notes are not included in the presentation.
5. Read **Automatic checks and remaining manual review**. Download the Excel,
   PowerPoint, English guide, check report or ZIP. Open the Office files yourself,
   verify the full brief, and submit yourself. This workflow never logs into an
   assessment platform or submits anything.

## Deployment

Install `requirements.txt`. The portable Streamlit runtime uses XlsxWriter,
python-pptx, Pillow and Matplotlib; it needs no local Microsoft Office, Node
runtime or shell execution. Excel chart XML is reused in PowerPoint so secondary
axes, cached data and chart types remain consistent across the two files.

Text planning uses the application's existing configured provider. Images use
the official OpenAI Images API independently, even if text uses Claude, Kimi or
Ollama. In Streamlit Community Cloud **Settings → Secrets**, configure:

```toml
STUDY_BUDDY_IMAGE_API_KEY = "your-private-openai-key"
```

`OPENAI_API_KEY` is also accepted. A temporary password field can hold an image
key for the current browser session. Keys are not exported or added to the
persisted progress/history allowlist. The default image model is
`gpt-image-1.5`; `STUDY_BUDDY_IMAGE_MODEL` can override it through the deployment
environment. Image quality is selected before each request. Consult the
[OpenAI image API guide](https://developers.openai.com/api/docs/guides/image-generation)
and [pricing](https://developers.openai.com/api/docs/pricing) for current model
access and charges. API access is separate from a ChatGPT subscription.

## Supported analysis

Plans support ordered column transformations, sorting/filtering, percentages,
lags, indices, explicit first-year proxies, row sums, seasonal ending years,
unpivoting wide tables, grouped aggregation, validated joins and equal-width
histograms with observed medians. Charts support line, column, horizontal bar,
area, scatter and pie. Line/column charts may use secondary axes.

There is no Python `eval`, generated script execution, network fetch or arbitrary
filesystem path in an analysis plan. Unknown operations, columns, zero
denominators, malformed periods, duplicate join keys and bounds that hide data
stop file creation. Strings from sources are written literally, not as formulas
or hyperlinks. Citation URLs must be present in the supplied brief/documents;
internal dataset citations must resolve to an actual uploaded dataset ID and
are credited using its filename, without creating a fictitious URL.

Limits are explicit: eight uploaded data tables; 20 derived tables; 20,000 rows,
80 columns and 200,000 cells per table; 500,000 cells overall; 12 charts and six
illustrations. Oversized or unsupported work requires a narrower plan rather
than silent truncation. An AI proposal is not a guarantee of requirement coverage.
The planning request has a 100,000-character context limit; oversized brief or
document content is rejected rather than silently dropping requirements.

## What the checks establish

The exporter reopens the saved workbook and compares every value and formula
presence with executed data, including cached formula results. It checks native
chart counts, series caches, XML, internal package relationships and embedded
workbooks. Histogram totals and unmatched join rows are recorded. Missing image
requests block PowerPoint export. Input or plan changes invalidate old downloads;
crop changes invalidate the presentation while preserving successful images.

These checks are not native Excel recalculation or a visual PowerPoint layout
inspection. They cannot certify academic correctness, factual background claims
or compliance with every assignment. Aggregation membership, histogram grouping,
filters and joins use a source snapshot: rebuild after changing source data.
Embedded PowerPoint workbooks are snapshots, not live links to the Excel file.
Tasks requiring native Excel screenshots, animations, specific editor operations
or other unsupported requirements retain a manual review step.

Artifacts stay in session memory, outside public course content and quiz banks.
Download them before a session expires or the server restarts. Source material
is shared with the configured text provider only when the planning button is
pressed; the image provider receives only the displayed image prompt.

## Verification

```sh
python -m unittest discover -s tests -p 'test_resolver_files*.py' -v
```

Tests use synthetic data and controlled API doubles. They exercise full-row
calculation, Office round trips, chart cache consistency, secondary axes,
literal source strings, invalid expressions, source references, image call
contracts, crop evidence, UI downloads and stale-output invalidation. A mocked
image API test does not establish that a deployment's OpenAI key has image access.
