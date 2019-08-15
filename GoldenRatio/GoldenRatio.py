Numbers = 20

currentNumber = 1
lastNumber = 0

print(str(lastNumber))

for x in range(0, Numbers):
	print(currentNumber)
	bufNum = lastNumber
	lastNumber = currentNumber
	currentNumber = bufNum + lastNumber
	
	