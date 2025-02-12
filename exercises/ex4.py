def add_to(n):
    if n == 0:
        return n
    else:
        return n + add_to(n - 1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num1 = int(input("Add to: "))
print(add_to(num1))
num2 = int(input("Factorial: "))
print(factorial(num2))
