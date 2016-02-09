from mrjob.job import MRJob
import re


class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        # yield "chars", len(line)
        # yield "words", len(line.split())
        # yield "lines", 1
		for word in re.sub("[^\w]", " ",  line).split():
			yield(word.lower(), 1)

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRWordFrequencyCount.run()
