"""Prepare the Mingshi corpus for collocation analysis (target: 内阁).

Steps
1. Load the raw plain-text source (Traditional) and convert to Simplified
   with OpenCC (t2s).
2. Split into sentences on 。！？……
3. Detect the 卷 (juan) header at the start of each 卷 (a line '卷X').
4. Segment every sentence with jieba, loading userdict.txt.
5. Cache data/segmented_sentences.txt and data/sentence_juan.txt.

Run from the repository root:  python code/prepare.py
"""
import re
import statistics

import jieba
from opencc import OpenCC

RAW = "data/mingshi.txt"
OUT = "data/segmented_sentences.txt"
JUAN = "data/sentence_juan.txt"
USERDICT = "userdict.txt"
TARGET = "内阁"

SENT_END = re.compile(r"([。！？\.!?……]+)")
JUAN_HEADER = re.compile(r"(?m)^\s*卷[一二三四五六七八九十百零〇]+\s*$")


def split_sentences(text):
    parts = SENT_END.split(text)
    sentences, buf = [], ""
    for part in parts:
        if SENT_END.fullmatch(part):
            buf += part
            if buf.strip():
                sentences.append(buf)
            buf = ""
        else:
            buf += part
    if buf.strip():
        sentences.append(buf)
    return sentences


def main():
    text = OpenCC("t2s").convert(open(RAW, encoding="utf-8").read())
    print(f"raw source      : {len(text)} characters (simplified)")
    print(f"  {TARGET}: {text.count(TARGET)} occurrences")

    jieba.load_userdict(USERDICT)
    jieba.initialize()

    sentences = split_sentences(text)
    labels, current = [], "(卷首)"
    segmented = []
    for sentence in sentences:
        header = JUAN_HEADER.search(sentence)
        if header:
            current = header.group(0).strip()
        labels.append(current)
        segmented.append([w for w in jieba.cut(sentence) if w.strip()])

    lengths = [len(s) for s in segmented]
    print(f"segmented       : {len(segmented)} sentences, "
          f"{sum(lengths)} tokens")
    print(f"tokens/sentence : median {statistics.median(lengths):.0f}, "
          f"max {max(lengths)}")
    print(f"distinct 卷     : {len(set(labels))}")

    with open(OUT, "w", encoding="utf-8") as f:
        for tokens in segmented:
            f.write(" ".join(tokens) + "\n")
    with open(JUAN, "w", encoding="utf-8") as f:
        f.write("\n".join(labels) + "\n")
    print(f"wrote {OUT} and {JUAN}")

    hits = sum(1 for tokens in segmented for w in tokens if w == TARGET)
    print(f"{TARGET} tokens in segmented corpus: {hits}")

    print("\n--- sample segmented sentences (eye check) ---")
    shown = 0
    for tokens in segmented:
        if TARGET in tokens:
            print(" ".join(tokens[:100]))
            shown += 1
            if shown == 5:
                break


if __name__ == "__main__":
    main()
