from collections import Counter
import re

def _merge_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

def replace(clicks):
    clicks = clicks.replace('blue', 'B')
    clicks = clicks.replace('red', 'R')
    clicks = clicks.replace('yellow', 'Y')
    clicks = clicks.replace('green', 'G')
    clicks = clicks.replace(',', '')
    return clicks

def remove_sequences(clicks):
    return re.sub(r"([A-Z])\1+", "\\1", clicks)

def find(clicks, counter):
    result = {}
    times=2
    length_a = len(clicks)
    for n in range(1,length_a/times+1)[::-1]:
        substrings=[clicks[i:i+n] for i in range(length_a-n+1)]
        freqs=Counter(substrings)
        fmc = freqs.most_common(1)[0][1]
        if fmc>=times and n > 1:
            seq=freqs.most_common(1)[0][0]
            for i in range(fmc):
                clicks = clicks.replace(seq, str(counter), 1)
                counter = counter + 1
            result[seq] = fmc
            r = find(clicks, counter)
            result = _merge_dicts(result, r)
            break
    return result