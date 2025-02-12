def greet():
    name = input("Enter name: ").split(" ")[-1]
    gender = input("Gender: ").lower()

    if gender == 'm':
        print("Greetings Mr. "+name)
    elif gender == 'f':
        print("Greetings Ms. "+name)
    else:
        print("Greetings "+name)

def largest(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

greet()

print(
    largest(
        int(input("\nFirst Number: ")),
        int(input("Second Number: ")),
        int(input("Third Number: "))
    )
)
