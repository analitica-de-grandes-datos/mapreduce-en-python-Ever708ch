#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import re

for line in sys.stdin:
    line = line.strip()
    fields = re.split(r'\s+', line)

    print(f'{fields[0]}\t{fields[1]}\t{fields[2]}')