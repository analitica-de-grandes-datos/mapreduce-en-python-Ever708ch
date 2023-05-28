#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split(',')
    print('%s\t%s' % (value, key))
