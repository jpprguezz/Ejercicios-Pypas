def run(text: str) -> bool:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    isalpha = True # Definimos a la variable como True de forma predeterminada.
    for letter in text.lower():
        if letter not in ALPHABET:
            isalpha = False
            break # El break hace que en el momento que no se encuentre algún carácter de la palabra en la constante, rompe el bucle.

    return isalpha


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
