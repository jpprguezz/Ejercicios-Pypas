def mcount(items: tuple[int], target: int = 1) -> int:
    """Calculate the frequency of target in items

    :param items: tuple representing all numbers
    :type items: tuple[int]
    :param target: number that we search
    :type target: int

    :return: The apparation frequency of target in items
    :rtype: int
    """
    target_frequency = 0
    for item in items:
        if item == target:
            target_frequency += 1
    return target_frequency



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(mcount)
