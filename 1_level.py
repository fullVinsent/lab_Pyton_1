import math

frustrumHeight = float(input("Input H:"))
smallRadius =float(input("Input r:"))
bigRadius = float(input("Input R:"))

frustrumLenght = math.sqrt(math.pow(frustrumHeight,2) + (math.pow(bigRadius - smallRadius,2)))

frustrumSideArea = math.pi * frustrumLenght * (bigRadius + smallRadius)

frustrumAllAreaSum = frustrumSideArea + (math.pi * math.pow(smallRadius,2)) + (math.pi * math.pow(bigRadius,2))

print(round(frustrumAllAreaSum,3))