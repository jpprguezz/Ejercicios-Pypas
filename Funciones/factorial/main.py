def factorial(n):
    result = 1
    if n < 0:
        return None
    else:
        for factorial_num in range(1, n + 1, 1):
            result *= factorial_num
        return result

            


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(factorial)
