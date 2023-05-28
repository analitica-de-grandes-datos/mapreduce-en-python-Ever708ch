#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
maximax = None
maximin = None

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t')
    value = float(value)

    if current_key == key:
        if value > maximax:
            maximax = value
        if value < maximin:
            maximin = value

    else:
        if current_key is not None:
            print(f'{current_key}\t{maximax}\t{maximin}')

        current_key = key
        maximax = value
        maximin = value

# Imprimir la última clave y su conteo acumulado
if current_key is not None:
    print(f'{current_key}\t{maximax}\t{maximin}')