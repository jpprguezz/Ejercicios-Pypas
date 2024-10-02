def run(hours: int, minutes: int, seconds: int) -> float:
    time_since_midnight = ((hours * 3600) + (minutes * 60) + seconds) * 1000
    return time_since_midnight


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
