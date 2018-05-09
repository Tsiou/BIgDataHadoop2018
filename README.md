# Big Data Hadoop 2018

This is a repository for the Lesson Big Data of University of Macedonia, Greece for the year 2018

Requirements:

Create a program that takes text files as input and outputs the words in the files whose length is bigger that the average word length on the files.

Implementation: 

Map:

Create a map function that receives input and outputs length of each word along with the world itself.

Map(text)
    <word, 1>

Combiner:

create a combiner that receives input <word, 1> and aggragates into <word, count>

Reducer: 

Reduce the output of the combiners to <sum(length), sum(count)>

output will be the total length and count for each reducer.

process the output to get a single value, sum(length)/sum(count) which is the average.

2nd map/reduce cycle:

Map:

Create a function that outputs <word, 1> (same mapper as stage 1)

Combiner: 

remove duplicates

Reduce:

for each word, get the length and emit it if length > average from 1st cycle.
