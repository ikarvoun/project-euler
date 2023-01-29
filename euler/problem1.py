#!/Applications/anaconda3/bin/python3 python3

x=1
y=0
for x in range(1, 100):
	if x%3 == 0 or x%5 == 0:
		y = y+x	
		print('This number is divisible ', y)
	else:
		print('This number is not divisible, ', x)
		pass

