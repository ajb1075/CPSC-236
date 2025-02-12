'''a = int(input("Positive integer 1: "))
b = int(input("Positive integer 2: "))

result = a if a < b else b

while result > 0:
    if ((a % result) == 0) and ((b % result) == 0):
        break
    result -= 1

print("\nGCD: {}".format(result))'''

for x in range(1,10):
    for y  in range(1,11):
        print("{}*{}={}".format(x, y, x*y), end=' ')
    print()
