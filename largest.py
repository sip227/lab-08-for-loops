numberList = []
for x in range(4):
	number = int(input("Number please..."))
	numberList.append(number)
	
if numberList[0] <= numberList[1]:
	x = numberList[1]
	if numberList[1] <= numberList[2]:
		x = numberList[2]
		if numberList[2] <= numberList[3]:
			x = numberList[3]
		elif numberList[2] >= numberList[3]:
			x = numberList[2]
	elif numberList[1] >= numberList[2]:
		x = numberList[1]
		if numberList[1] <= numberList[3]:
			x = numberList[3]
		elif numberList[1] >= numberList[3]:
			x = numberList[1]
elif numberList[0] >= numberList[1]:
	x = numberList[0]
	if numberList[0] <= numberList[2]:
		x = numberList[2]
		if numberList[2] <= numberList[3]:
			x = numberList[3]
		elif numberList[2] >= numberList[3]:
			x = numberList[2]
	elif numberList[0] >= numberList[2]:
		x = numberList[0]
		if numberList[0] <= numberList[3]:
			x = numberList[3]
		elif numberList[0] >= numberList[3]:
			x = numberList[0]
			
print("The largest number is ", x)
    
