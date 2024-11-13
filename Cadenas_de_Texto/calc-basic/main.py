def run():
    num_1 = int(input("Introduce el primer número: "))
    num_2 = int(input("Introduce el segundo número: "))
    print(num_1, "+", num_2, "=", num_1 + num_2, sep=''), "\n"
    print(num_1, "-", num_2, "=", num_1 - num_2, sep=''), "\n"
    print(num_1, "*", num_2, "=", num_1 * num_2, sep=''), "\n"
    print(num_1, "/", num_2, "=", num_1 / num_2, sep=''), "\n"


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
