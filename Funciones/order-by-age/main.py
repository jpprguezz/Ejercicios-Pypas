def order_by_age(people: list[dict]) -> list[dict]:
    result = (sorted(people, key=lambda t: t.values()))
    return result






# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(order_by_age)
