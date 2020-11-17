days = [31,28,31,30,31,30,31,31,30,31,30,31]
day=int(input('Введите номер дня:'))
m=1
if (day>days[i]):
	m=m+1
	day=day-days
	print('Месяц:', m, ' ', 'День:', day )
else:
	print('Месяц:', m, ' ', 'День:', day )
