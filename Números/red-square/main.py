def run(arc_A: float) -> float:
    PI = 3.14
    circle_diameter = (arc_A * 4) / PI
    radius = circle_diameter / 2
    area = radius * radius
    return round(area, 10)


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
