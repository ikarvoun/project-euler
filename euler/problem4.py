#!/Applications/anaconda3/bin/python3 python3


def palindrome(a):
	for i in range(2,a):
		for j in range(2,a):
			#palindrome check
			tempi = i
			tempj = j
			tempij = i*j
			rev=0
			while (tempij>0):
				digit = tempij%10
				rev = rev*10 + digit
				tempij = tempij//10
			if (tempij==rev):
				print(tempij , 'which is product of ' ,i, ' and ' ,j, ': is a palindrome ')	
			else:
				pass
			
	return

def main():
	#a=int(input("Please enter the first digit (999 to check for up to 3 digits): "))
	#b=int(input("Please enter the second digit (999 to check for up to 3 digits): "))
	a=999
	print(palindrome(a))


if __name__ == "__main__":
	main()
