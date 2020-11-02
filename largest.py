highestnum = 0
for x in range(4):
	userinput = input("Number please... ")
	usernum = int(userinput, 10)
	if usernum > highestnum:
		highestnum = usernum
		print("Updating highestnum... ")
	else: 
		print("This is not the highest number")
	
	
			
print("The largest number is ", highestnum)
    
