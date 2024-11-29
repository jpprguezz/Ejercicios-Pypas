def run(items: list) -> int:
    sum_items = sum([int(item) for item in items])  # Recorremos la lista completa conviertiendo cada número de ella en entero y luego los sumamos todos 

    return sum_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
