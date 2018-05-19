import math
import sys

list =[]

for line in sys.stdin:
    list += [int(s) for s in line.split() if s.isdigit()]
    

average = math.floor(float(list[0])/float(list[1]))
print('%s' % average)
