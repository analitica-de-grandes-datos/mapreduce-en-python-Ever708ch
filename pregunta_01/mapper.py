#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    # Eliminar espacios en blanco iniciales y finales
    line = line.strip()

    # Dividir la línea en campos (atributos)
    fields = line.split(',')

    # Extraer el campo credit_history (índice 2 en la lista fields)
    credit_history = fields[2]

    # Emitir el par clave-valor (credit_history, 1)
    print(f'{credit_history}\t1')