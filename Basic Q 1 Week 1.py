##Week 1 Task 1

##Write a function that randomnly shuffles an array of integers and
##explain the rationale behind its implementation

array = [5, 3, 8, 6, 1, 9, 2, 7] #Create array of random integers
import random

for i in range(0, 7):  #Loop from 0 to array length
	y = random.randint(0, i) #Create temp list of random numbers from loop
	if y == i: #If it is the same create it again
		continue 
	array[i], array[y] = array[y], array[i] #Replace temp list with actual array
print(array
