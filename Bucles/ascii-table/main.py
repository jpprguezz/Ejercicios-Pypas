def run(start_code: int, end_code: int) -> None:
    counter = 0
    for code in range(start_code, end_code + 1):
        formatted_code = f"{code:03d}"
        caracter = chr(code)
        print(f"{formatted_code} {caracter}", end="   ")
        counter += 1
        if counter % 5 == 0:
            print()

# POR COMENTAR

# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
