"""Restartable iterable over the cached segmented corpus.

``find_collocates`` iterates the corpus twice, so it needs an iterable that
can be re-iterated. This class opens the file fresh on every ``__iter__``.
"""
SEGMENTED = "data/segmented_sentences.txt"


class SegmentedCorpus:
    def __init__(self, path=SEGMENTED):
        self.path = path

    def __iter__(self):
        with open(self.path, encoding="utf-8") as f:
            for line in f:
                tokens = line.split()
                if tokens:
                    yield tokens
