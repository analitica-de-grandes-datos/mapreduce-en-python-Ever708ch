#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    # Eliminar espacios en blanco iniciales y finales
    line = line.strip()

    # Dividir la línea en campos (atributos)
    fields = line.split(',')

    # Emitir el par clave-valor (credit_history, 1)
    print(f'{fields[3]}\t{fields[4]}')