# Schedule and submission records

Course Plan, Overview and Progression Plan use one English schedule view. Next up selects the current or next scheduled course that has no recorded submission or completion. Open course navigates to its Learn & Practice overview. Detailed lessons and Noroff course availability are separate.

Upcoming deadlines are chronological and respect Course Plan's semester and literal text search filters. Recorded submissions are separate; unrecorded past deadlines and historical module events are collapsed. Calendar passage never supplies completion or grade evidence. Resubmissions use a Needs attention group and direct the learner to Noroff for the new deadline; the original date is labelled explicitly.

Use Update submission status to record a submission date, a passed result or a required resubmission, or correct a record back to No submission recorded. These are personal records, not a Noroff sync. They are saved through the existing Study Buddy state file on the running app instance. As with the rest of this local state, cloud instance replacement can reset it. Future submission dates are rejected and write failures keep the previous record and show an error. Older course-completion flags are labelled as user-recorded completion, not an automatically verified grade. Submission records do not award learning progress or credits.

The JAN 2026 FT schedule dates come from Noroff's progression workbook updated 22 September 2026, checked 16 October 2026. All countdown dates use Europe/Oslo. Year 2 dates remain unverified. Actual attempt timers and any individually granted extensions must be checked on Noroff.

Validation: run `python -m unittest discover -s tests -p 'test_study_schedule*.py'`. Tests cover false completion prevention, status/date validation, storage reload/failure, legacy completion flags, filters/empty states, resubmissions, and Streamlit navigation/status updates.
