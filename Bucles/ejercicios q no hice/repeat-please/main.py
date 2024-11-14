def run():
    while True:
        name_surname = input("¿Su nombre? ")
        if name_surname.istitle():
            break
        else:
            print("Error. Debe escribirlo correctamente")


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
