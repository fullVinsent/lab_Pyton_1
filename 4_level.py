import random

sum = 0
listOfNumbers = []
x = 0

while x < 10:
    x += 1
    while sum < 20:
        number = random.randint(0,2)
        sum += number
        listOfNumbers.append(number)
        if sum > 20:
            sum -= number
            listOfNumbers.pop(-1)
        print(number)
    print(sum)
    print(listOfNumbers)


