# The Company 内阁 Keeps in the *Mingshi*

**Name:** minzhangecho
**Course:** DHG 502 — Assignment 1
**Target word:** 内阁 (the Grand Secretariat / inner cabinet)

## Research question

How does the *Mingshi* (明史, History of the Ming) present the 内阁 as an
institution? Which words does 内阁 keep company with more often than chance,
and what do they show about the way the Qing compilers describe the Grand
Secretariat — its functions (drafting edicts, deliberating state affairs), its
place among the 六部 / 九卿, and the officials who staffed it?

## Source

- **Text:** 張廷玉 et al., 《明史》, compiled at the Qing court and completed
  in 1739; 332 卷.
- **Edition used:** the plain-text UTF-8 course template `明史.txt`
  (Traditional characters). A public, citable edition is on Wikisource:
  <https://zh.wikisource.org/wiki/明史>.
- **Size processed:** 3,279,015 characters → 170,503 sentences /
  2,095,352 tokens after segmentation. 内阁 appears 297 times as a token.
- **Rights:** the *Mingshi* (1739) is in the public domain. The plain-text
  transcription comes from the course template and is used for coursework.

## Repository layout

```
data/
  mingshi.txt                raw source (UTF-8, traditional)
  segmented_sentences.txt    cached jieba segmentation (one sentence per line)
  sentence_juan.txt          卷 label for each sentence in the cache
userdict.txt                 jieba user dictionary (institutions/offices/names)
code/
  prepare.py                 opencc -> sentence split -> jieba -> cache
  corpus.py                  restartable iterable over the cache
  collocations.py            runs find_collocates (window 5, window 10, sentence)
  concordance.py             qhchina.kwic for the discussed collocates
  build_html.py              renders output/results.html and output/kwic.html
output/
  collocates_window5.csv
  collocates_window10.csv
  collocates_sentence.csv
  kwic.csv
  results.html
  kwic.html
report.md / report.pdf       the essay
AI-USE.md                    AI-use disclosure
requirements.txt
```

## How to run

Install dependencies and run the scripts **from the repository root**:

```bash
pip install -r requirements.txt
python code/prepare.py        # ~1-2 min: builds data/segmented_sentences.txt
python code/collocations.py   # writes output/collocates_*.csv
python code/concordance.py    # writes output/kwic.csv
python code/build_html.py     # writes output/results.html, output/kwic.html
```

## Processing decisions

1. **Conversion.** Traditional source → Simplified with OpenCC (`t2s`); the
   target is written `内阁`.
2. **Sentence splitting.** On runs of `。！？.!?……` — 170,503 sentences
   (median 10 tokens, longest 1,033).
3. **Segmentation.** jieba with `userdict.txt`, tailored to this question:
   the institution 内阁 and its offices (首辅, 次辅, 大学士, 票拟, 批红,
   司礼监, 六部, 九卿, 都察院, 给事中 …) and the Grand Secretaries who held
   office (杨廷和, 李东阳, 张璁, 夏言, 严嵩, 徐阶, 高拱, 张居正, 申时行 …).
4. **Stopwords.** `load_stopwords("zh_cl_sim")` (classical Chinese, simplified)
   inside `find_collocates`. No custom stopwords were added.
5. **Filters and correction.** `min_word_length=2`, `correction="fdr_bh"`,
   `max_adjusted_p=0.05`, `measures=["log_likelihood", "logDice"]`,
   `alternative="greater"`.
6. **No homograph or surname-dropping problem:** 内阁 is an unambiguous
   two-character institution term.

## Segmentation check (by eye)

The target and the main office words segment correctly (`内阁`, `大学士`,
`首辅`, `司礼监`, `文华殿`), but jieba (modern dictionary) still errors:

- artifacts that appear as spurious collocates: `一送`, `官入`, `专用词`,
  `房中` — merged across word boundaries; they are treated as noise, not
  evidence;
- occasional over-merges like `召对 内阁` fine, but `官侍 朝立` shows
  neighbouring words merged.

The substantive collocates (机务, 拟旨, 中书, 六部, 九卿, 舍人, 杨廷和,
刘健) are stable across the three runs.

## Outputs

- `output/collocates_*.csv` — one CSV per run, with contingency-table counts,
  Fisher `p_value`, `adjusted_p_value`, `log_likelihood`, `log_dice`.
- `output/results.html` — all three tables on one page.
- `output/kwic.html` — concordance lines (with 卷 labels) for the collocates
  discussed in the report.
