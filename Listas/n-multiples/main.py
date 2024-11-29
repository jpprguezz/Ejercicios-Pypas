def run(x: int, n: int) -> list:
    calc = [x * num for num in range(n + 1)]  # Creamos una lista por compresión en la que multiplicamos x por el item del iterable, que pilla los numeros dentro del rango del numero n
    multiples = calc[1:]  # Como nos añade el elemento 0 de la lista no lo necesitamos, troceamos la lista desde el elemento 1 hacia el final 
    return multiples


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
