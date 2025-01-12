def run(number: int) -> list:
    rev_digits = []  # Le asignamos le valor de lista vacía para guardar los números
    number_formatted = list(str(number))  # Formateamos el numero primero a string, para poder convertirlo luego a lista
    reversed_number_formatted = reversed(number_formatted)
    for char in reversed_number_formatted:  # Recorremos el numero ya convertido en lista y reverseado 
        rev_digits.append(int(char))  # Añadimos cada uno de los caracteres (pasados a enteros) y los añadimos a la lista
    return rev_digits


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
