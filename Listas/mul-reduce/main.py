def run(numbers: list) -> int:
    rmult = 1  # Igualamos la variable a uno para que los números que se vayan añadiendo se multipliquen por si mismos y se vaya haciendo la asignación aumentada
    for number in numbers:  # Recorremos la lista
        rmult *= number  # Vamos añadiendo los números múltiplicados a la lista
    return rmult


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
