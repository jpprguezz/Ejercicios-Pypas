def run(xmin: int, xmax: int) -> list:
    values = [(3 * num + 2) for num in range(xmin, xmax + 1)]
    return values


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
