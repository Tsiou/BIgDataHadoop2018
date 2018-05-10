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

average = wordsum/wordcount

print('%s' % average)