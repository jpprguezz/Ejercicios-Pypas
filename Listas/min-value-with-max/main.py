def run(values: list) -> int:
    min_value = max(values)  # Pillamos el mayor número de la lista usando la función max()
    for value in values:  # Recorremos la lista 
        if value < min_value:  # Comparamos el valor con el valor máximo y si es menor:
            min_value = 0  # Igualamos la variable a 0
            min_value += value  # Y le añadimos el nuevo valor
    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
