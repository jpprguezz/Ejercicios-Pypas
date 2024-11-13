def run(target_number: int) -> None:
    tries = 0
    while True:
        selected_num = int(input("Introduzca número: "))
        tries += 1
        if selected_num < target_number:
            print("Mayor")
        elif selected_num > target_number:
            print("Menor")
        else:
            print(f"Enhorabuena has encontrado el número en {tries} intentos")
            break

# POR DOCUMENTAR
# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
