#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
suma = 0
count_values = 0
for line in sys.stdin:

    line = line.strip()
    key, value, count = line.split('\t')
    value = float(value)

    if current_key == key:
        suma += value
        count_values += int(count)

    else:
        if current_key is not None:
            print(f'{current_key}\t{suma}\t{suma/count_values}')

        current_key = key
        suma = value
        count_values = int(count)

# Imprimir la última clave y su conteo acumulado
if current_key is not None:
    print(f'{current_key}\t{suma}\t{suma/count_values}')