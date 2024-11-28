def run(values: list) -> int:
    min_value = values[0]  # Usamos el primer elemento de la lista para poder empezar a comparar este número con el resto
    for value in values:  # Recorremos la lista valor por valor
        if value < min_value: # Si algún valor es menor que el primer elemento de la lista
            min_value = 0  # Reiniciamos la variable a 0 y le sumamos asignamos el nuevo valor
            min_value += value

    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
