import sys

values = sys.argv[1:]  # El argumento dado en forma de string
values_to_int = [int(v) for v in values]  # Pasamos a entero cada elemento del string, y gracias a la compresión, se queda automaticamente guardado en esta lista
result = sum(values_to_int) / len(values_to_int)  # Calculamos el promedio
print(f'{result:.2f}')  # Lo representamos con dos decimales
