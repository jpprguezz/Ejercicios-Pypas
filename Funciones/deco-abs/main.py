def fabs(func):
    def wrapper(*args, **kwargs):
        return func(abs(*args), abs(**kwargs))
    return wrapper

@fabs
def run(a, b):
    return (a, b)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
