def run(n: int) -> float:
    if n == 0:
        fibo = 0
    elif n == 1:
        fibo = 1
    a = 0
    b = 1
    for _ in range(2, n + 1):
        calc = a + b
        a = b
        b = calc
    fibo = b
    return fibo

# POR DOCUMENTAR
# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
