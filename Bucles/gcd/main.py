def run(a: int, b: int) -> int:
    gcd_value = 1
    for divisor in range(1, a + 1):
        if a % divisor == 0 and b % divisor == 0:
            gcd_value = divisor
    return gcd_value

# POR DOCUMENTAR
# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
