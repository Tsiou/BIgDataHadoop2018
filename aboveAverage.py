from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class aboveAverage(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            if len(word) > 5:
                yield word, 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    aboveAverage.run()
