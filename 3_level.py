firstAngle = input("Input first angle:")
secondAngle = input("Input second angle:")

if int(firstAngle) == int(secondAngle) == 60:
    print("Трикутник рівносторонній")
elif int(firstAngle) == int(secondAngle):
    print("Трикутник рівнобедренний")
elif 180 - (int(firstAngle) + int(secondAngle)) == int(firstAngle):
    print("Трикутник рівнобедренний")
elif 180 - (int(firstAngle) + int(secondAngle)) == int(secondAngle):
    print("Трикутник рівнобедренний")
elif int(firstAngle) == 90 or int(secondAngle) == 90:
    print("Трикутник прямокутний")
elif int(firstAngle) + int(secondAngle) == 90:
    print("Трикутник прямокутний")
elif int(firstAngle) > 90 or int(secondAngle) > 90:
    print("Трикутник тупокутній")
elif int(firstAngle) + int(secondAngle) < 90:
    print("Трикутник тупокутній")
else:
    print("Трикутник гострокутній")