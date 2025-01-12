def run(items: list) -> bool:
    item_to_compare = items[0]  # Usamos el primero elemenot de la lista para comparar
    all_same = True  # Colocamos el valor de la variable ne True por defecto
    for item in items:  # Recorremos la lista
        if item != item_to_compare: # Si alguno de los elementos es diferente a el elemento a comparar, automáticamente es falso
            all_same = False
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
