def run(values: list) -> int:
    max_value = values[0] # El primer número de la lista, que lo utilizaremos para empezar a comparar números
    for value in values: # Se recorre la lista
        if value > max_value: # Se compara si el numero es mayor que el valor máximo
            max_value = 0 # Si lo es, se iguala la variable a cero y se asigna el nuevo número
            max_value += value

    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
