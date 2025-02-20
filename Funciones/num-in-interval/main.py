def in_range(value: int, /, lower_limit: int, upper_limit: int, ) -> bool:
    if value in range(lower_limit, upper_limit + 1):
        return True
    return False


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(in_range)
