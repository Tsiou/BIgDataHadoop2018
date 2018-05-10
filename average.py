#test function
import sys

for line in sys.stdin:

    line = line.strip()
    words = line.split()
    
average = sum(len(word) for word in words) / len(words)

print('%s', average)