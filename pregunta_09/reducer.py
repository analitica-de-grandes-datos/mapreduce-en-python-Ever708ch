#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_letter = None
values = []

for line in sys.stdin:
    line = line.strip()
    key, date, value = line.split('\t')

    values.append((key, date, int(value)))
sorted_values = sorted(values, key=lambda x: x[2])

for i in range(6):
    key, date, values = sorted_values[i]
    print(f'{key}   {date}   {values}')