##Week 1 Task 2

##Count the number of trailing 0s in a factorial number

x = int(input("input number"))
import math
x = math.factorial(x) #Change user input to it's factorial

def zeroes(x):
    result = 0 #Output value of 0s
    for i in range(2, x + 1):          
        while x > 0:
            if x % 5 == 0: #Exactly divisible by 5 with remainder 0
                result += 1 #Add one to output
                x = x / 5
            else:
                break
    print(result)
    
zeroes(x)
