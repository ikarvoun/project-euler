#!/Applications/anaconda3/bin/python3 python3

def isPrime(j):
	count = 0
	for i in range(2,j):
		if j%i==0:
			count = count+1
		else:
			pass
	if count == 0:
		return True
	else:
		return False		
	
def primefactorCheck(num):
	sumofPrimes=0
	if num > 1:
		for j in range(2,int(num/2)+1):
			#check for factor
			if num%j==0:
				print(j , ' is a factor ')
				#
				#check if factor is prime
				if isPrime(j) == True:
					print(j,' is also a prime')
				#	insert any artithmetic required
					sumofPrimes=j+sumofPrimes
					print('current sum of all primes in this sequence: ' , sumofPrimes)	
			else:
				pass

	else:
		print("Enter a higher number, please")
	return


def main():
	num=int(input("Please enter the number you'd like to find prime factors for: "))
	primefactorCheck(num)


if __name__ == "__main__":
	main()
