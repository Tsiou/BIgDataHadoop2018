# Big Data Hadoop 2018

This is a repository for the Lesson Big Data of University of Macedonia, Greece for the year 2018

Requirements:

Create a program that takes text files as input and outputs the word and count of the words with a length bigger that the average word length in the files.

Implementation: 

2 cycles of mapreduce.
-- Cycle 1: output: sum(chars), sum(wordcounts)

-- Input files, get the average value sum(chars)/sum(wordcounts)

-- Cycle 2: output: word, wordcount

Details:

Map:

Create a map function that receives input and outputs length of each line along with the num of words in the line.

Reducer: 

Reduce the output of the combiners to <sum(length), sum(count)>.

process the output to get a single value, sum(length)/sum(count) which is the average.

2nd map/reduce cycle:

Map:

Create a function that outputs <word, 1> if length of word is bigger than average found above.

Reducer:

Sum the occurences of each word, returning <word, sum(counts)>.
