#Mapper Class for our program
import sys

for line in sys.stdin:

    #getting a line and removing whitespace
    line = line.strip()

    #split line into words
    words = line.split()

    for word in words:
        print('%s\t%s' % (word.length, word))
