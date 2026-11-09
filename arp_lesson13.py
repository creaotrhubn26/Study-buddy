"""Original referencing study material and Task 1.3 scaffolds, not a submitted essay."""

from pathlib import Path

ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "arp"
TEMPLATE_ROOT = ASSET_ROOT / "templates"
COURSE_CODE = "FI1BBAR05"
LESSON_URL = "https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81688"
TASK_URL = "https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81698"
CHECKED_ON = "2026-11-09"
SCHOLAR_URL = "https://scholar.google.com/scholar?q=%22data+analyst%22+workplace+enterprise+analysis"
BOUNDARY = (
    "Task 1.3 asks for a 500-word overview titled 'The Data Analyst in the Workplace', with at least four citations "
    "followed by a Bibliography/Reference list in Harvard style. Use Google Scholar to find a few good sources. "
    "The brief says at least four citations, not explicitly four distinct sources. Four separate sources may add breadth, "
    "but are not a stated minimum. No Harvard institutional variant, word-count inclusion rule, tolerance, file format, "
    "font, page count, required software or mandatory figures is specified. Confirm the Harvard variant and whether "
    "references and in-text citations count toward 500 words; do not invent a ±10% allowance. "
    "The five-paragraph word budget is a Study Buddy suggestion, not an official marking scheme. "
    "Cite paraphrases as well as quotations; match each citation to a verified reference and supporting passage. "
    "Never fabricate an author, year, title, DOI, quotation, page locator, source-reading claim or completed review. "
    "Scholar and citation generators are discovery/formatting aids, not the original evidence. The lesson's John Doe "
    "sources are dummy demonstrations and must not be cited as real research. Chicago examples are not the required "
    "Harvard style. Starter papers are optional, not an approved Noroff reading list or proof that the learner has read them. "
    "Exam Resolver reviews the supplied draft and source notes in English; it cannot certify unread sources, native Word "
    "formatting, an official word count or a submission from a written plan. The learner checks the saved file and submits it."
)
RESOLVER_REQUEST = (
    "Review my 500-word workplace overview and citation/evidence plan in English. Explain my selected step. "
    "Check the stated word-count rule, at least four in-text citations, matching Harvard references, claim-to-source "
    "support and source-reading status. Flag placeholders and unverified metadata. Suggest improvements to my own "
    "paragraphs without inventing citations, quotations, page numbers or claims that I read a paper. "
    "If my body text is still blank, help me plan it rather than claiming a finished 500-word overview."
)
STEPS = [
    (
        "1. Decode the overview brief",
        "Record the exact topic: The Data Analyst in the Workplace. Plan a 500-word overview, at least four in-text citations and a following Harvard reference list. Confirm the institution's Harvard variant and what counts toward 500 words. The brief gives no word-count tolerance or required file format.",
        "Distinguish an overview of the workplace role from an essay about citation software. Four citations does not automatically mean four distinct sources.",
    ),
    (
        "2. Search Google Scholar and screen sources",
        "Start with the linked Scholar search, then refine terms such as data analyst competencies, enterprise data analysis, and knowledge sharing data analysts. Open the original article or author/publisher page, not just a search snippet. Check author, year, title, publication, DOI, relevance and access. Record whether you read the full text or only the abstract. The starter cards below are optional research leads.",
        "A result in Scholar is not proof of peer review or accuracy. Do not claim to have read a paywalled full paper when you only saw its abstract.",
    ),
    (
        "3. Build a claim-to-source evidence matrix",
        "For each planned claim, write a source ID, your own note, the supporting section or real page locator, and the limits of that evidence. Plan at least four citation placements across the overview. Reusing a relevant source is allowed by the wording; use a sensible range for breadth. Never invent a page number or turn an interview finding into a universal fact about every workplace.",
        "Every source-backed claim can be traced to a passage actually consulted. Blank evidence cells remain unresolved rather than becoming invented support.",
    ),
    (
        "4. Plan five focused paragraphs",
        "Use this optional 500-word budget: role and purpose 70; data preparation 120; analysis and interpretation 110; communication and responsibility 130; conclusion 70. The total is 500. Explain the role, how data becomes useful evidence, and how findings support decisions. Connect paragraphs rather than listing software. Adapt the budget if the tutor's counting rule includes references or citations differently.",
        "The five-paragraph plan is a scaffold, not a required structure. Avoid promising universal tools, guaranteed business outcomes or causal effects unsupported by your sources.",
    ),
    (
        "5. Draft and insert Harvard citations",
        "Write in your own words from your evidence notes. Place author-date citations next to the claims they support, for example (Kandel et al., 2012) or Collier and Powell (2024). Cite paraphrases too. For a direct quotation, reproduce the exact wording and add a verified page or other locator required by the chosen Harvard guide. Prefer concise paraphrases in a short overview.",
        "There are at least four meaningful in-text citation placements. A reference list alone is not four citations. Do not copy text and merely change a few words.",
    ),
    (
        "6. Build and cross-check the reference list",
        "Create an alphabetical list with full details for every cited source, following one agreed Harvard variant. Check authors, publication year, title, journal, volume, issue, page range and DOI against the original publication record. A journal article's whole page range is not the pinpoint page of a quotation. Use Word, Zotero, Mendeley Cite or manual formatting as available, then verify their output.",
        "Every in-text citation has a matching entry, and every reference-list entry is cited. If using a broader bibliography, label consulted-only items according to the tutor's guidance rather than pretending they were cited.",
    ),
    (
        "7. Review the word count and saved document",
        "Read for focus, evidence and clear English. Apply the tutor's confirmed counting rule; use Word's count on the relevant text and record the result. Check at least four citations, alphabetical Harvard entries, claim support and unresolved placeholders. Save and reopen your work. Prepare Task 1.3 in Exam Resolver to review the draft and notes; make final corrections in your document and submit it yourself.",
        "An AI estimate is not an official Word count or proof that the sources support your claims. The task does not require the conceptual images to be included in your submission.",
    ),
]
PARAGRAPHS = [
    (
        "Role and purpose",
        70,
        "Explain why the workplace needs the analyst and what decisions the work can inform.",
    ),
    (
        "Data preparation",
        120,
        "Explain acquiring, understanding and checking data before analysis; map a citation to actual evidence.",
    ),
    (
        "Analysis and interpretation",
        110,
        "Explain suitable methods, interpretation and uncertainty; distinguish association from causation.",
    ),
    (
        "Communication and responsibility",
        130,
        "Connect findings to readers and decisions; discuss limits and appropriate handling of data without inventing legal rules.",
    ),
    (
        "Conclusion",
        70,
        "Bring together the role's value and the need for evidence, context and clear communication. Introduce no unsupported finding.",
    ),
]
SOURCES = [
    dict(
        id="S1",
        citation="(Kandel et al., 2012)",
        reference="Kandel, S., Paepcke, A., Hellerstein, J.M. and Heer, J. (2012) 'Enterprise data analysis and visualization: An interview study', IEEE Transactions on Visualization and Computer Graphics, 18(12), pp. 2917–2926. doi: 10.1109/TVCG.2012.219.",
        url="https://idl.uw.edu/papers/enterprise-analysis-interviews",
        use="Research lead for the enterprise analyst's activities and organisational context. The abstract describes interviews with 35 analysts across 25 organisations; this is a study sample, not a universal definition of the role.",
        checked="Author-hosted abstract and publication/DOI record checked. Read the paper and record the supporting passages before using detailed claims.",
    ),
    dict(
        id="S2",
        citation="(Collier and Powell, 2024)",
        reference="Collier, C.A. and Powell, A.L. (2024) 'Data analyst competencies: A theory-driven investigation of industry requirements in the field of data analytics', Journal of Information Systems Education, 35(3), pp. 325–376. doi: 10.62273/SPYC4248.",
        url="https://aisel.aisnet.org/jise/vol35/iss3/8/",
        use="Research lead for entry-level knowledge, skills and dispositions. Its abstract describes a theory-based model and hiring-manager survey; findings have a study context, not a guarantee of all current employer requirements.",
        checked="Journal-hosted abstract, authors, issue, page range and DOI checked against the journal's publication record. Detailed claims need full-text reading.",
    ),
    dict(
        id="S3",
        citation="(Ghasemaghaei, 2023)",
        reference="Ghasemaghaei, M. (2023) 'Does knowledge sharing belief of data analysts impact their behavior?', Journal of Computer Information Systems, 63(2), pp. 460–478. doi: 10.1080/08874417.2022.2070799.",
        url="https://www.tandfonline.com/doi/abs/10.1080/08874417.2022.2070799",
        use="Research lead for sharing analytical insights in organisations. The publisher's abstract describes a study of knowledge-sharing beliefs and behaviour. Do not assert an intervention causes better decisions from the title alone.",
        checked="Publisher-indexed abstract and bibliographic details checked. The issue is 2023; online-first publication was 2022. Use the year consistently for the version cited. Full text was not reviewed.",
    ),
]
CHECKS = [
    (
        "Topic and length",
        "The overview addresses the workplace role and meets 500 words under the confirmed counting rule; no invented tolerance.",
    ),
    (
        "At least four citations",
        "Count in-text citation placements and check the source/claim link, not just bibliography entries.",
    ),
    (
        "Harvard reference list",
        "One Harvard variant, alphabetical entries and complete verified metadata after the overview.",
    ),
    (
        "Two-way matching",
        "Each in-text citation matches a reference; reference-list entries are cited in the text.",
    ),
    (
        "Evidence and final file",
        "The actual passages were consulted, quotations/locators checked, placeholders removed and saved file reopened.",
    ),
]
QUESTION_TEMPLATE = """# ARP Task 1.3 Overview and evidence plan

Planning scaffold only, not a completed 500-word answer or an official solution.

## Brief and decisions
Title: The Data Analyst in the Workplace
Target: 500 words; at least four in-text citations; following Harvard Bibliography/Reference list
Google Scholar search terms and date: [...]
Harvard institutional variant or tutor clarification: [...]
Does the word count include in-text citations, title/headings and references? [...]
Confirmed counting rule: [...]
No word-count tolerance is stated in the brief.

## Source-reading record
S1 author/year, original URL/DOI and publication details: [...]
S1 actual access: [not read / abstract only / full text]; relevant passage and limits: [...]
S2 author/year, original URL/DOI and publication details: [...]
S2 actual access and supporting passage: [...]
S3 author/year, original URL/DOI and publication details: [...]
S3 actual access and supporting passage: [...]
Additional sources if useful: [...]

## Five-paragraph working budget (suggested, totals 500)
1. Role and purpose: 70 words
2. Data preparation: 120 words
3. Analysis and interpretation: 110 words
4. Communication and responsibility: 130 words
5. Conclusion: 70 words
Adjust if the confirmed counting rule includes references or citations differently.

## Overview body — write your own prose here
[Paragraph 1: role, purpose and a supported claim with a citation.]
[Paragraph 2: data preparation and a citation tied to a passage you read.]
[Paragraph 3: analysis, interpretation, uncertainty and a supporting citation.]
[Paragraph 4: communication/responsibility and a supporting citation.]
[Paragraph 5: bring together the supported points without new unsupported claims.]

## References — Harvard variant confirmed above
[Full entry for every cited source, in alphabetical order.]
[The three optional starter cards are research leads, not sources you can claim to have read automatically.]

## Four citation placements to verify
1. Claim [...]; author/year [...]; supporting passage/locator [...]
2. Claim [...]; author/year [...]; supporting passage/locator [...]
3. Claim [...]; author/year [...]; supporting passage/locator [...]
4. Claim [...]; author/year [...]; supporting passage/locator [...]
Four citations are required; four distinct sources are not explicitly prescribed.

## Final check notes
Word count in saved document, selected text and counting rule: [...]
At least four in-text citations checked: [Not checked]
Every citation matches an alphabetical Harvard reference: [Not checked]
Every reference-list entry is cited: [Not checked]
Claim support, quotations and real locators verified: [Not checked]
Sources actually read and limitations recorded: [Not checked]
Placeholders removed and saved file reopened: [Not checked]
Outstanding issue and next action: [...]
"""
ILLUSTRATIONS = [
    dict(
        file="lesson-1-3-evidence-referencing.png",
        title="From evidence to Harvard referencing",
        caption="Read the source, write an accurate paraphrase, add an author-date citation and provide a matching full reference. Paraphrases need citations too. Check generated metadata and follow one Harvard variant. The conceptual illustration does not certify the truth of a claim or replace a source.",
    ),
    dict(
        file="task-1-3-overview-plan.png",
        title="Build a 500-word overview",
        caption="Suggested paragraph budgets are 70 + 120 + 110 + 130 + 70 = 500 words. Include at least four in-text citations and a matching Harvard reference list. Confirm the counting rule with the tutor. This is a Study Buddy planning aid, not an official marking scheme or a requirement to add images to the overview.",
    ),
]
GUIDE = dict(
    course_code=COURSE_CODE,
    id="1.3-task",
    uid="arp-1.3-task-81698",
    lesson_number="1.3",
    title="The Data Analyst in the Workplace — Harvard-referenced overview",
    source_url=TASK_URL,
    method="Harvard-referenced workplace overview",
    deliverable="A 500-word workplace overview with at least four citations, followed by a Harvard Bibliography/Reference list",
    steps=[s[1] for s in STEPS],
    caution=BOUNDARY,
    task_dataset="",
    template_file="ARP Task 1.3 Overview and Evidence Plan.md",
)
LESSON_CONTENT = """### Lesson 1.3 Referencing Styles and Tools

Referencing makes borrowed ideas, words, data and images traceable to their sources. It helps the reader check what supports a claim and distinguishes your contribution from earlier work. Credibility depends on the quality and relevance of the evidence, not simply on adding a citation.

### 1 Link the claim, citation and full reference

A short **in-text citation** identifies the source near the relevant claim. A **full reference** supplies enough publication information to locate it. A **reference list** normally contains the works cited in your text; a **bibliography** may also include relevant works consulted, depending on the required guide. Cite a source when its idea informs your writing even if you do not quote its exact words. Avoid treating a list of things you read as proof of support for every sentence.

Paraphrasing means explaining the source's meaning accurately in your own structure and wording, with a citation. A direct quotation keeps the exact words, clearly marked as a quotation, and adds the locator required by the chosen guide. Do not invent page numbers. Images, charts and adapted figures also need appropriate attribution; citing a source is not the same as permission to reuse it. The conceptual Study Buddy images are optional learning aids, not required Task 1.3 figures.

### 2 Recognise the main styles without mixing them

| Style | Typical citation system | End list | Key distinction |
|---|---|---|---|
| Chicago | Notes and bibliography **or** author-date | Bibliography or reference list, matching the chosen system | Chicago has two systems; do not mix note and author-date examples indiscriminately |
| APA | Author-date | References | Cite paraphrases; use the required locators for quotations; APA is not automatically the required Harvard variant |
| MLA | Usually author-page, with the available locator | Works Cited | A source without pages cannot supply an invented page number; notes can still serve explanatory purposes |
| Harvard | Author-date, with local variations | Usually an alphabetical reference list | The institution's version controls punctuation, author shortening, locators and online-source details |

The Noroff examples mix some conventions. Chicago is not exclusively parenthetical, and APA/MLA do not categorically prohibit explanatory notes. Do not reuse the lesson's APA or Chicago formatting for a Harvard task. [Chicago's own two-system guide](https://www.chicagomanualofstyle.org/tools_citationguide.html) explains that distinction. See also the [APA citation guide](https://apastyle.apa.org/style-grammar-guidelines/citations) and [MLA citation overview](https://style.mla.org/in-text-citations-overview/). For Task 1.3, confirm Noroff's expected Harvard version. [Leeds Harvard basics](https://library.leeds.ac.uk/info/1402/referencing/50/leeds_harvard_introduction) is an example of an institutional version, not a claim that Noroff requires Leeds Harvard.

### 3 Practise Harvard with real source metadata

A common pattern is a narrative citation, **Collier and Powell (2024)**, or a parenthetical citation, **(Collier and Powell, 2024)**. A multi-author example is **(Kandel et al., 2012)**. Exact shortening and punctuation depend on the selected Harvard guide. Place the citation so the supporting claim is clear; one citation at the end of a long paragraph may not make all borrowed ideas traceable.

For a journal article, a common full-reference pattern is: Author surname, initials (year) 'Article title', Journal title, volume(issue), page range, DOI. Use the source's actual details, not this template's placeholders. A whole-article page range belongs to the reference; a specific quotation or passage locator belongs to the citation when required. Cite the version actually consulted and keep its year consistent. Never claim a quote was verified from an abstract if the quote is not there.

### 4 Use Word and generators as aids

Desktop Word offers source management, inserted citations and bibliography tools through References; exact controls and style choices vary by edition. Select the required Harvard variant if supported, add accurate source metadata, insert citations where needed, then generate and check the end list. Selecting APA in the lesson demonstration does not satisfy a Harvard brief. Its John Doe/Test citation/Lorem ipsum examples are fictional training records, not research sources.

An online generator can arrange entered metadata, but it cannot guarantee that the author, year, title or source type is correct or that the source supports a claim. Check against the original article or publisher record. Availability, accounts and supported styles can change; do not assume a named tool is free, accountless or offers your Harvard variant. Manual referencing is also possible when checked consistently.

### 5 Distinguish Zotero from Mendeley Cite

Zotero can organise source records in collections, store reading notes and help insert citations and bibliographies in supported editors. In desktop Word, its plugin uses Add/Edit Citation, Add/Edit Bibliography, Document Preferences and Refresh. A bibliography entry is not inserted with the citation command alone. Correct metadata in the library and refresh; manual edits in an active bibliography may be overwritten. [Zotero plugin instructions](https://www.zotero.org/support/word_processor_plugin_usage/).

For your browser-based Word workflow, do not expect the desktop Zotero tab to appear automatically: Zotero's documentation says its Word Online plugin is not available, although Word Online can preserve existing Zotero fields. You can create and carefully check a manual list, or use a supported alternative. [Zotero's compatibility note](https://www.zotero.org/support/kb/existing_citations_not_detected).

Mendeley Reference Manager organises references; **Mendeley Cite** is its Word add-in. The official listing includes Word on the web, but availability may depend on your Microsoft account or institution's add-in policy. If available, choose a Harvard style, insert real citations and then a bibliography, and check both. Do not download the lesson's fixed old Windows installer as if it were required on your Mac. Installing citation software is not a task requirement. [Official Mendeley Cite listing](https://store.office.com/addinsinstallpage.aspx?assetid=WA104382081&isWac=True&rs=en-001).

### 6 Find and evaluate reading material

Google searches can find a broad range of material; Google Books may offer a limited preview rather than a full book; Google Scholar helps discover scholarly literature, versions and citation trails. Search for the topic, refine terms and open the actual publication. A search snippet or automatically generated citation is not the evidence itself. Check relevance, author expertise, publication type, method, date, access and limitations. Scholar results include different publication types and are not all peer reviewed.

The Scholar search for **“data analyst” workplace enterprise analysis** located the optional source leads below. Kandel et al. (2012) examines enterprise analysis in its organisational setting; Collier and Powell (2024) examines entry-level competencies; Ghasemaghaei (2023) examines knowledge-sharing beliefs and behaviour. These are useful starting points for different paragraphs, not an approved reading list or evidence that you personally read the papers. Source cards state what was checked and what still needs reading. Do not infer all current employers' requirements from one study.

### 7 Apply the lesson to Task 1.3

Write a **500-word overview of “The Data Analyst in the Workplace”**, with **at least four citations**, followed by a **Harvard Bibliography/Reference list**. Use Google Scholar to find a few good sources. The brief does not explicitly require four distinct sources, a particular Harvard variant, software, illustrations, file format or a word-count tolerance. Confirm whether citations, headings and references count toward the target.

Use the optional 70/120/110/130/70 paragraph budget, trace each main claim to your reading notes, and include at least four meaningful citation placements. A source can be cited more than once when relevant; breadth is useful but should not become an invented minimum. End with an alphabetical matching reference list. Review the saved document and its count before submitting it yourself. Exam Resolver can review your draft and notes in English; it cannot certify unread sources or native Word layout from a plan.

**Exam explanation pattern:** claim → source passage → accurate paraphrase → author-date citation → matching full reference → check relevance and limits. Tools reduce formatting work; they do not replace reading and verification.
"""


def source_cards_markdown():
    text = "### Optional research leads\n\nOriginal Study Buddy starter cards, not an approved Noroff reading list or an official answer. The examples use one common Harvard author-date pattern; adapt it to the tutor's required variant. No claim is made that the learner has read these papers.\n\n"
    for source in SOURCES:
        text += f"#### {source['id']} · {source['citation']}\n{source['reference']}\n\n[Original publication record]({source['url']})\n\nPossible use: {source['use']}\n\nReading status: {source['checked']}\n\n"
    return text.rstrip() + "\n"


def guide_markdown():
    text = (
        "## ARP Task 1.3 Workplace overview and Harvard referencing\n\n"
        + BOUNDARY
        + "\n\n"
    )
    for title, instruction, check in STEPS:
        text += f"### {title}\n{instruction}\n\nCheck: {check}\n\n"
    text += "### Suggested paragraph budget\n" + "\n".join(
        f"- {title}: {words} words. {purpose}" for title, words, purpose in PARAGRAPHS
    )
    text += "\n\n### Final checks\n" + "\n".join(
        f"- **{title}:** {detail}" for title, detail in CHECKS
    )
    # Keep the main guide compact enough for both regular and strict resolver contexts.
    return (
        text
        + f"\n\n[Original task]({TASK_URL}) · [Google Scholar search]({SCHOLAR_URL}). Checked {CHECKED_ON}. The templates and guide are original Study Buddy learning scaffolds.\n"
    )
