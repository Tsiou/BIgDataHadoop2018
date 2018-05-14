from mrjob.job import MRJob

class aboveAverage(MRJob):

    def mapper(self, _, line):
        
        words = line.split()
        for word in words:
            if len(word) > average:
                yield (word, 1)

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)
        


if __name__ == '__main__':
    aboveAverage.run()
