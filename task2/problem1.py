x = input("enter the numbers: ")
y = []
z = ""

for i in x :
    if i == " ":
        if z:
            num = int(z)
            if num == -1:
                break
            y.append(num)
            z = ""
    else:
        z += i

print(max(y) , min(y))