##Week 5 Task 1

##Given a sequence of n integer numbers, extract the sub-sequence of maximum
##length which is in ascending order.

import random
seq = random.sample(range(0, 50), 20) #Create random sequence with integers between 0 and 50 length 20
newseq = [1] #Temporary output

def seq_extractor(seq, newseq): #Function: Counts for each ascending pair and adds it to newseq
	count = 1
	
	for i in range(0, len(seq)):
		if i == len(seq) - 1:
			break
		else:
			if seq[i] < seq[i+1]:
				count += 1
				newseq.append(count)
			elif seq[i] > seq[i+1]:
				count = 1
				newseq.append(count)
				
#Example of newseq [1, 1, 2, 3, 1, 1, 2, 3, 4, 1, 1]
				
seq_extractor(seq, newseq)

temp = newseq.index(max(newseq)) #Takes highest value in newseq
output = [] #New temporary output

for i in range(1, max(newseq)+1): #Takes all the values prior, noting down there posistion to temp up to the first 1 it finds
	output.append(temp)
	temp -= 1

output.reverse()
new = [] #Final temporary output

for j in output: #Taking the output e.g. [1, 2, 3]
                 #Takes those values out of the initial sequence
	new.append(seq[j])

print(seq)
print(new)
