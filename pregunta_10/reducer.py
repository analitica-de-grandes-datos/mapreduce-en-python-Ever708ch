#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
numbers = []

for line in sys.stdin:
    line = line.strip()
    key, number = line.split('\t')
    number = int(number)
    if current_key is None:
        current_key = key

    if key == current_key:
        numbers.append(number)
    else:
        print(f' {current_key}\t{",".join(str(i) for i in sorted(numbers))}')
        current_key = key
        numbers = [number]

# Output the last key's numbers

print(f' {current_key}\t{",".join(str(i) for i in sorted(numbers))}')