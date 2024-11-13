def run():
    for part_1 in range(7):
        for part_2 in range(part_1, 7):
            print(f"{part_1}|{part_2}", end=" ")
        print()

# POR DOCUMENTAR
# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
