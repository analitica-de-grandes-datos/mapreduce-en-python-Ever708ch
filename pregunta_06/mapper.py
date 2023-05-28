#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('   ')

    print(f'{fields[0]}\t{fields[2]}')