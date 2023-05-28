#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split('\t')
    if len(columns) == 2:
        key = columns[0]
        letters = columns[1].split(',')
        for letter in letters:
            print('%s\t%s' % (letter, key))