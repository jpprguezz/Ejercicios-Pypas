def run(texts: list) -> list:
    formatted_texts = "".join(texts)
    chars = []
    for letter in formatted_texts:
        chars.append(letter)
    return chars


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
