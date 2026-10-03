"""Concordance lines (KWIC) for the 内阁 collocates discussed in the report.

Run from the repository root:  python code/concordance.py
"""
import csv

from qhchina import kwic

from corpus import SegmentedCorpus

KWIC_TARGETS = ["机务", "学士", "拟旨", "中书", "六部", "九卿"]

JUAN = "data/sentence_juan.txt"
OUT = "output/kwic.csv"
HORIZON = 10


def main():
    labels = open(JUAN, encoding="utf-8").read().splitlines()

    df = kwic(
        SegmentedCorpus(),
        KWIC_TARGETS,
        horizon=HORIZON,
        sort_by="position",
    )
    df["juan"] = [labels[i] if i < len(labels) else "" for i in df["doc_index"]]

    cols = ["juan", "node", "left", "right", "doc_index", "position"]
    df[cols].to_csv(OUT, index=False, encoding="utf-8", quoting=csv.QUOTE_ALL)

    print(f"{len(df)} concordance lines for {len(KWIC_TARGETS)} collocates")
    for node, group in df.groupby("node", sort=False):
        print(f"  {node}: {len(group)} lines")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
