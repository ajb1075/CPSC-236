ls = [int(input("Enter an integer: ")) for i in range(15)]
item = int(input("Look for: "))
print(
    "{}\n{}\nMin: {}\nMax: {}".format(
        l := [0 if i == item else i for i in ls],
        s := sorted(l),
        s[0],
        s[-1]
    )
)
      
