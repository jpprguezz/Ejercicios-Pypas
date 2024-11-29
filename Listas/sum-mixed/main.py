def run(items: list) -> int:
    sum_items = 0  # Seteamos la variable a 0
    for item in items:  # Recorremos la lista
        int_item = int(item)  # Creamos una variable que guarda item pero en entero
        sum_items += int_item  # Se lo sumamos a la variable
    return sum_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
