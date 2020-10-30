userinput = input("Let's party! How long until the party? ")
usernum = int(userinput, 10)
if usernum < 1:
    print("PARTY NOW!!!")
else:
    for i in range(usernum, 0, -1):
        print(i)
        if i == 1:
            print("PARTY TIME!!!")




