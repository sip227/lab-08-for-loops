myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}

keys = []

values = []


for k, v in myData.items():
	print("key:", k, ", value:", v)
	keys.append(k), values.append(v)
	
	
print("ALL KEYS:", str(keys))
print("ALL VALUES:", str(values))
 