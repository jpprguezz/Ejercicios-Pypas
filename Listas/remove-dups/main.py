def run(nums_dups: list) -> list:
    nums_unique = [] # Esta será la cadena en la que se almacenen los números no repetidos
    for num in nums_dups:
        if num in nums_unique: # Si el numero ya se encuentra en la lista, lo pasa
            continue
        else: # Si no, lo añade
            nums_unique.append(num)
    return nums_unique


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
