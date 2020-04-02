number = input("Input number:")
sum = 0
multiple = 1

for x in number:
    sum += int(x)
    multiple *= int(x)

print("Sum:" + str(sum))
print("Multiple:" + str(multiple))