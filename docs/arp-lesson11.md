# Analysis Reporting Lesson 1.1

Course FI1BBAR05 now includes the reviewed Lesson 1.1 Report Writing and Task 1.1 in Learn & Practice and ARP Module 1 in Training Center.

Sources read while signed in on 9 November 2026:
- [Lesson 1.1](https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81667) and its What is a Report, Importance, Introduction, Preparing, Report Structure and review chapters (81668–81673).
- [Task 1.1](https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81674).

The task concerns a small handmade-candle business, Facebook, Instagram and TikTok, no paid advertising, and the last six months. The deliverable is questions ordered from general to specific, with attention to posting schedule and content type. It supplies no data or exact calendar dates and prescribes no word count, font or file format. The official downloadable solution was not opened or used. Lesson explanations, example questions and templates are original Study Buddy study material. The UI distinguishes the required question plan from an optional full-report outline.

Assets in `assets/arp` contain two original PNGs generated with the built-in OpenAI imagegen tool. Their exact prompts and attribution are included in `imagegen-prompts.json` and `IMAGE_CREDITS.md`. The readable English captions explain the visuals without relying on image text. No measured social-media performance is depicted.

Downloads: question plan Markdown, blank question-to-evidence CSV matrix, optional report outline Markdown, current personal draft Markdown and both PNGs. The CSV can be opened in Excel. No dataset or calculation workbook is invented for this planning task.

The seven-step selector and applied draft carry into the existing Universal Exam Resolver. ARP task guides are searchable sources, exact Task 1.1 matching selects its guide, and normal and strict AI modes receive the selected step, draft and task boundaries in English. The question-planning answer style avoids inventing engagement findings. Changes to draft/step/source controls invalidate old answer context. No automatic AI request or Noroff submission occurs on handoff.

Personal drafts and step selections use the existing Study Buddy state file; download a copy because cloud instance replacement can reset local state.

Validation: `python -m unittest discover -s tests -p 'test_arp_lesson11.py'` exercises the actual app, lesson resources, seven steps, templates, handoff, draft persistence, normal/strict provider request contracts and Training Center. Paid text-provider calls are replaced with an offline response in these tests. Image generation was actually performed with the built-in tool, and the output was visually inspected. Browser verification additionally checks native app rendering, CSV download bytes and lesson-to-resolver navigation.
