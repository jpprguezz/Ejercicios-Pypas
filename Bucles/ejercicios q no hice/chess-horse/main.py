def run(target_x: int, target_y: int) -> int:
    x_movements = 0
    y_movements = 0
    turns = 0
    while x_movements < target_x and y_movements < target_y:
        x_movements += 2
        y_movements += 2
        turns += 1
        x_movements += 1
        y_movements += 2
        turns += 1
        if x_movements == target_x and y_movements == target_y:
            movements = turns
        elif target_x and target_y not in range(0, 10):
            movements = -1
    return movements


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
