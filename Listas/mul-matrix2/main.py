def run(A: list, B: list) -> list:
    num1= (A[0][0] * B[0][0]) + (A[0][1] * B[1][0])  # Simplemente consiste en usar los indices de las listas para ir haciendo las operaciones
    num2 = (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
    num3 = (A[1][0] * B[0][0]) + (A[1][1] * B[1][0])
    num4 = (A[1][0] * B[0][1]) + (A[1][1] * B[1][1])
    P = [[numerator_1, denominator_1], [numerator_2, denominator_2]]  # Se representan los numeradores y denominadores en dos listas dentro de una lista para obtener el resultado
    return P


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
