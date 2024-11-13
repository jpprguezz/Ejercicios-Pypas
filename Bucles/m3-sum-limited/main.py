def run(limit: int) -> None:
    sum_of_nums = 0
    multiples_of_limit = 0
    while sum_of_nums < limit:
        print(multiples_of_limit, end=" ") # Esto es lo que se mostrará en pantalla al ejecutar el programa
        sum_of_nums += multiples_of_limit
        multiples_of_limit += 3


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
