##Week 2 Task 3

##Write the pseudocode for a function which returns the highest perfect square
##which is less or equal to its paramater. Implement this in python

##PSEUDOCODE

#INPUT = INPUT(integer)

#FUNCTION nearest_square(INPUT):
#	OUTPUT = 0
#	INPUT = square root(INPUT)
#	INPUT = round down(INPUT)
#	OUTPUT = INPUT * INPUT
#	PRINT(OUTPUT)
	
#CALL nearest_square(INPUT)


##ACTUAL CODE
x = int(input("input number"))
import math

def nearest_square(x):
	result = 0
	x = math.sqrt(x) #Square root it
	x = math.floor(x) #Round it down
	result = x*x #Square it back up to give result
	print(result)
	
nearest_square(x)
