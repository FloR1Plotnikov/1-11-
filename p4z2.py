import math
n = int(input("Введите значение n="))
k = int(input("Введите значение k="))
summ = 0
i=1
while n >= i:
    summ = summ + math.sqrt(k*i)
    i=i+1
    print (i)
    print (summ)
print (summ)
