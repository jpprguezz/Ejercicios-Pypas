def run(n: int) -> list:
    powers2 = []  # Se crea la lista vacia para guardar los números
    for i in range(0, n + 1): # Se hace un bucle for para recorrer los numeros desde el 0 al indicado
        powers2.append(2**i) # Se añade a la lista el el resultado de 2 elevado al número que corresponda
    return powers2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
