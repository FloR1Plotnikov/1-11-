import math
T=1-0.99
x1, y1, r1=map(int, input('Введите координаты первого круга:').split())
x2, y2, r2=map(int, input('Введите координаты второго круга:').split())
print(T)
d=(math.sqrt((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))
if(abs(x1-x2)<T) and (abs(y1-y2)<T) and (abs(r1-r2)<T):
	print('Круги совпадают!')
elif (d>r1+r2+T):
	print('Круги не пересекаются!')
elif (abs(d-(r1+r2))<=T):
	print('Круги соприкасаются!')
elif (d<r1+r2):
	if (d>abs(r1-r2)):
		print('Круги пересекаются!')
	else:
		print('Один круг в другом!')
