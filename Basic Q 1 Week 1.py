array = [5, 3, 8, 6, 1, 9, 2, 7]
import random
for i in range(0, 7):
	y = random.randint(0, i)
	if y = i:
		continue
	array[i], array[y] = array[y], array[i]
print(array)
