def run(u: list, v: list) -> float | None:
    length_u = len(u)  # Calculamos longitud de las dos listas
    length_v = len(v)
    dprod = None  # Seteamos dprod a None desde el principio
    if length_u == length_v:  # En el momento que tengan la misma longitud, el valor de dprod pasa de ser None a 0 para poder sumar valroes dentro
        dprod = 0
        for u_num, v_num in zip(u, v): # Hacemos el zip de las dos listas
            dprod += u_num * v_num # Añadimos el resultado de la multiplicacion de los dos elementos y los va sumando poco a poco
    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
