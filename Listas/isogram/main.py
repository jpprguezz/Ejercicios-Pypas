def run(text: str) -> bool:
    isogram = True  # Colocamos por defecto la variable en True
    appeared_letters = [] # Creamos una lista para ir guardando las letras que vaya viendo el for
    for letter in text:
        if letter == "-":  # Si la letra es igual a un '-', la pasa
            continue
        if letter not in appeared_letters:  # Si la letra no esta todavía en la lista vacía, la mete ahi
            appeared_letters.append(letter)
        else:
            isogram = False  # Y si lo está, ya no es un isograma, por lo que paramos de buscar con un break
            break

    return isogram


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
