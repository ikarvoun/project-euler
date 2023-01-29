#!/Applications/anaconda3/bin/python3 python3

#nterms = int(input("How many terms? :"))
maxValue = int(input("Enter the maximum fibonacci term: "))

# first two terms
n1, n2, sumVal = 0 , 1, 0
count = 0

# check if the number of terms is valid
if maxValue <= 0:
	print("Please print a positive integer\n")
# ifthere is only one term, return N1
if maxValue  == 1:
	print ("Fibonacci sequence up to " , maxValue, ":")
	print(n1)
else:
	print("Fibonacci sequence: \n")
	while n1 < maxValue:
		print(n1)
		if n1%2 == 0:
			sumVal=n1+sumVal
		else:
			pass
		nth = n1 + n2
		#update values
		n1 = n2
		n2 = nth
		count += 1

print('\n\nSum of the even valued integers: ' , sumVal)

