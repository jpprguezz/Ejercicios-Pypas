def split_case(words: list[str]) -> list[str]:
    upper_case_words = []
    lower_case_words = []
    for word in words:
        if word.isupper():
            upper_case_words.append(word)
        elif word.islower():
            lower_case_words.append(word)
    return lower_case_words, upper_case_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(split_case)
