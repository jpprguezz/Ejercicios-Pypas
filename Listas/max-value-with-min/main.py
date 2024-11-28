def run(values: list) -> int:
    max_value = min(values)  # Encontramos el mínimo con la función min()
    for value in values:  # Recorremos la lista
        if value > max_value:  # Se compara si value es mayor que el valor mínimo
            max_value = 0  # Si lo es, se iguala la variable a 0 y se le asigna el valor 
            max_value = value
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
