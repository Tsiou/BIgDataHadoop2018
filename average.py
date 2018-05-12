import math
import sys

list =[]

for line in sys.stdin:
    list += [int(s) for s in line.split() if s.isdigit()]
    

average = math.floor(float(list[1])/float(list[0]))
print('%s' % average)
