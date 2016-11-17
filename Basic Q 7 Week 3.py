##Week 3 Task 7

##Write a recursive function to check if a number n is prime

x = int(input("input your number"))
temp = 2

def prime(temp, x):
	if x <= 1:
		print("Is not prime")
	else:
		if temp == x:
			print("Is prime")  #Special base case cause temp = 2
		else:
			if (x % temp) == 0: #Exactly divisible with remainder 0
				print("Is not prime")
			else:
				return prime(temp+1, x)

prime(temp, x)


##PSEUDOCODE

#Prompt user for number to check if it's a prime or not (x)
#Temporary value of 2 held

#FUNCTION prime(temp, x)
#IF x <= 1
#       PRINT "Is not prime"
#ELSE
#       If temp == x:
#               PRINT "Is prime"
#       Else:
#               If x is exactly divisible by temp with remainder 0
#                       print "Is prime"
#               Else:
#                       RETURN FUNCTION(temp+1, x)
