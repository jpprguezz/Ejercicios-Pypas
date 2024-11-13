def run(n: int) -> tuple:
    sum_of_nums = 0
    right_side = 0
    for num in range(1, n + 1):
        sum_of_nums += num
        right_side += num ** 3
    left_side = sum_of_nums ** 2
    return left_side, right_side

# POR DOCUMENTAR
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
