def run(A: list, B: list) -> list:
    numerator_1 = (A[0][0] * B[0][0]) + (A[0][1] * B[1][0])
    denominator_1 = (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
    numerator_2 = (A[1][0] * B[0][0]) + (A[1][1] * B[1][0])
    denominator_2 = (A[1][0] * B[0][1]) + (A[1][1] * B[1][1])
    P = [[numerator_1, denominator_1], [numerator_2, denominator_2]]
    return P


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
