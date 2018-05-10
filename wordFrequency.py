from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class wordFrequency(MRJob):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
     wordFrequency.run()