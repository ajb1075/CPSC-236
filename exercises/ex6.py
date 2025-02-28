def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)

def power(base: float, exp: int) -> float:
    return base ** exp

if __name__ == '__main__':
    f = int(input("Enter number to make factorial: "))
    print(f"{f}! = {factorial(f)}")

    b = float(input("\nEnter the base: "))
    e = int(input("Enter the exponent: "))
    print(f"{b}^{e} = {power(b, e)}")
    
