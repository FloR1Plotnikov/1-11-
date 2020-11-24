import math
n=int(input('Введите n='))
e=int(input('Введите e='))
i=0
summ=0
while i <= n :
	i=i+1
	summ=summ+(((math.pow(-1, i))* i)/math.pow(2, i))
	print(i)
	if (summ<=e):
		print(summ)
	else:
		break	
print(summ)
