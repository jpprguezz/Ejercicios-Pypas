import sys

values = sys.argv[1:]
values_to_int = [int(v) for v in values]
result = sum(values_to_int) / len(values_to_int)
print(f'{result:.2f}')
