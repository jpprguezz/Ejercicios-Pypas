def run(price_with_igic: float, igic: float) -> float:
    index_variation = (igic / 100) + 1
    clean_price = price_with_igic / index_variation
    return round(clean_price, 2)


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
