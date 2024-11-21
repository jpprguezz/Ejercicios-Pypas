def run(u: list, v: list) -> float | None:
    length_u = len(u)
    length_v = len(v)
    dprod = None
    if length_u == length_v:
        dprod = 0
        for u_num, v_num in zip(u, v):
            dprod += u_num * v_num
    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
