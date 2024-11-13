def run():
    for i in range(1, 10):
        num = int("1" * i) # Se multiplica el 1 en forma de string por el numero de veces que se necesitan para esa linea, y se va haciendo las escalera de multiplicaciones que vemos en el enunciado
        result = num * num
        print(result)


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
