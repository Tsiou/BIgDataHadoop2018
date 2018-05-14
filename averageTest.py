#test function
import sys

wordsum = 0
wordcount = 0

for line in sys.stdin:

    line = line.strip()
    words = line.split()
    for word in words:
        wordsum += len(word)
        wordcount +=1

average = math.floor(wordsum/wordcount)

print('%s\t%s\n%s\t%s\n%s\t%s\n' % ("average: ",average, "sum: ", wordsum, "count: ", wordcount))