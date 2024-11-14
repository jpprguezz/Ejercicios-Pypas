def run():
    for i in range(1, 10):
        num = int("1" * i)
        result = num * num
        print(result)


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
