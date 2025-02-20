def is_perfect(n: int) -> bool:
    def n_divisors(n: int) -> list[int]:
        [i for i in range(1, n + 1) if i % n == 0]



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_perfect)
