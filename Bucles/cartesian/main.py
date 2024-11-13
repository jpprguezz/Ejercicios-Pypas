def run(text1: str, text2: str) -> str:
    cartesian = ""
    for letter1 in text1:
        for letter2 in text2:
            cartesian += letter1 + letter2
    return cartesian


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
