#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
maximax = 0

for line in sys.stdin:
    # Eliminar espacios en blanco iniciales y finales
    line = line.strip()

    # Dividir la línea en clave y valor
    key, value = line.split('\t')

    # Convertir el valor (string) a int
    value = int(value)

    # Verificar si la clave actual es igual a la clave leída
    if key == current_key:
        if value > maximax:
            maximax = value
    else:
        # Si la clave actual no es None, imprimir la clave actual y su conteo acumulado
        if current_key is not None:
            print(f'{current_key}\t{maximax}')

        # Actualizar la clave actual y reiniciar el conteo
        current_key = key
        maximax = value

# Imprimir la última clave y su conteo acumulado
if current_key is not None:
    print(f'{current_key}\t{maximax}')