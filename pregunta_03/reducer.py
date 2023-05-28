#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

data = []

for line in sys.stdin:
    line = line.strip()
    value, key = line.split('\t')
    data.append((int(value), key))

data.sort()

for value, key in data:
    print('%s,%s' % (key, value))