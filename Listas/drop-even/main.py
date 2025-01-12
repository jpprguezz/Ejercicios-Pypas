def run(items: list) -> list:
    even_nums = []  # Le asignamos una lista vacía para guardar los numeros pares (los cuales no necesitamos)
    filter = []  # Le asignamos una lista vacía para guardar los números impares (los cuales si queremos)
    for item in items:  # Recorremos la lista
        if items.index(item) % 2 == 0:  # Si al dividir entre dos la posición del item en la lista da cero, significa que es par, por lo que lo añadimos a la lista de números pares
            even_nums.append(items)
        else:  # Si no se cumple la primera condición, significa que el número es impar, por lo que lo añadimos a la listade numeros impares
            filter.append(item)
    return filter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
