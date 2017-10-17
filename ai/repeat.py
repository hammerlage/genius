import re
from random import randint
from collections import Counter

def ra(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

clicks = "blue,blue,red,blue,green,red,yellow,red,red,green,yellow,blue,red,red,green,green,yellow,blue,red,yellow,green,red,blue,blue,yellow"

clicks = clicks.replace('blue', 'B')
clicks = clicks.replace('red', 'R')
clicks = clicks.replace('yellow', 'Y')
clicks = clicks.replace('green', 'G')
clicks = clicks.replace(',', '')

#print list(repetitions(clicks))
c = 0
def count(a, c):
    times=2
    for n in range(1,len(a)/times+1)[::-1]:
        substrings=[a[i:i+n] for i in range(len(a)-n+1)]
        freqs=Counter(substrings)
        fmc = freqs.most_common(1)[0][1]
        if fmc>=times and n > 1:
            seq=freqs.most_common(1)[0][0]
            for i in range(fmc):
                a = a.replace(seq, str(c), 1)
                c = c + 1
            print "sequence '%s' of length %s occurs %s or more times"%(seq,n,times)
            print a
            count(a, c)
            break
print clicks
count(clicks, 0)