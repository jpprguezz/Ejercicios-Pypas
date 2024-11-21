def run(input_date: str, base_year: int) -> str:
    date_whitout_bars = input_date.split("/")  # Para obetener una lista solo con los numeros
    day = f"{int(date_whitout_bars[1]):02d}"  # El día, el cual debe poseer obligatoriamente 2 caracteres
    month = f"{int(date_whitout_bars[0]):02d}"  # El mes, el cual debe poseer obligatoriamente 2 caracteres
    year = f"{int(date_whitout_bars[2]) + base_year:04d}" # El año, el cual debe poseer obligatoriamente 4 caracteres más el año base
    new_date_elements = [day, month, year]  # Los guardamos en una nueva lista
    reorganizated_date = "-".join(new_date_elements)  # Usamos join para que los separadores entre números sean "-"
    output_date = reorganizated_date
    return output_date

# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
