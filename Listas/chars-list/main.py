def run(texts: list) -> list:
    formatted_texts = "".join(texts) # Unimos el texto quitando los espacios para poder usarlo todo junto
    chars = []  # Creamos una lista vacia para guardar las letras que veamos con el bucle
    for letter in formatted_texts: # Recorremos el texto
        chars.append(letter) # Añadimos cada letra a la listga vacia
    return chars


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
