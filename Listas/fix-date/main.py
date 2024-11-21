def run(input_date: str, base_year: int) -> str:
    date_whitout_bars = input_date.split('/')
    day = f'{int(date_whitout_bars[1]):02d}'
    month = f'{int(date_whitout_bars[0]):02d}'
    year = f'{int(date_whitout_bars[2]) + base_year:04d}'
    new_date_elements = [day, month, year]
    reorganizated_date = '-'.join(new_date_elements)
    output_date = f'{reorganizated_date}'
    return output_date


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
