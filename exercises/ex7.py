from operator import mul
from functools import reduce

def sumprod(first: int, second: int) -> int:
    return sum(range(first, second+1)), reduce(mul, range(first+1, second+1), first)

if __name__ == '__main__':
    first = int(input("First Number: "))
    second = int(input("Second Number: "))
    s, p = sumprod(first=first, second=second)
    print(f"\nSum: {s}\nProduct: {p}")
