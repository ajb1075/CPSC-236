D = {}

for i in range(5):
    item = input("\nItem: ")
    score = float(input("Score: "))
    D[item] = score

DS = {k: v for k, v in sorted(D.items(), key=lambda item: item[1])}

print(DS)
