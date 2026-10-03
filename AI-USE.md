# AI-USE.md

This file discloses how AI tools were used, following the course-wide
requirements. (Adjust to the exact template if the course provides one.)

## Tools used

- An AI coding assistant was used to help write and debug the Python scripts
  in `code/` and to explain the `qhchina` API.

## What the AI helped with

- Writing `prepare.py` (OpenCC conversion, sentence splitting, jieba
  segmentation, 卷 detection, caching) and the other scripts.
- Writing `collocations.py`, `concordance.py`, and `build_html.py`, including
  the `find_collocates` / `kwic` arguments.
- Troubleshooting the `卷X` header parsing and the `SegmentedCorpus`
  restartable iterator.
- Drafting the repository structure and this disclosure.

## What the student did

- The research question, choice of target (内阁), interpretation of results,
  and all analytical prose in `report.md` / `report.pdf` were written by the
  student without AI generation.
- The student checked a sample of segmented sentences by eye.

## Prompts / dialogue

The main use was an iterative coding session (build the pipeline, run it,
inspect outputs, fix bugs). No AI-generated text was pasted into the report
without being rewritten in the student's own words.
