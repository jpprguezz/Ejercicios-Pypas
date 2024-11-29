def run(numers: list) -> int:
    result = 0  # Se iguala la variable a cero para sumar en ella valores 
    for number in numers:  # Se recorre la lista
        if number < 0:  # Si el número es menos que cero (es decir, si es negativo), se pasa
            continue
        else:  # Si no, se suma a la variable inicial
            result += number
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
