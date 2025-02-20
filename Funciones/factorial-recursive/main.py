def factorial(n: int) -> int | None:
    if n == 0:
        return 1
    if n < 0:
        return None
    return n * factorial(n - 1)



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(factorial)
