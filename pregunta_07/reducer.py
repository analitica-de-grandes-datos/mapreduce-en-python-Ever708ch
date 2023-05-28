#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_letter = None
values = []

for line in sys.stdin:
    line = line.strip()
    key, date, value = line.split('\t')

    if current_letter is None:
        current_letter = key

    if key == current_letter:
        values.append((date, int(value)))
        
    else:
        if current_letter is not None:
            sorted_values = sorted(values, key=lambda x: x[1])
            for d, v in sorted_values:
                print(f'{current_letter}   {d}   {v}')
            current_letter = key
            values = [(date, int(value))]
        date = date

sorted_values = sorted(values, key=lambda x: x[1])
for date, val in sorted_values:
    print(f'{current_letter}   {date}   {val}')