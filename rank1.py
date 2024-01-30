#New file for every br
#One main file to call all other files (index), can either use it as a library or a menu

User_Tank = str(input('What tank are you in? \n'))
usaSet = {"M2A4", "M2" , "LVT(A)(1)", "M13 MGMC"}

#for tanks in usaSet:
    #print(tanks)

if User_Tank in usaSet:
    print('Scanning for other tanks')
else:
    str(input('Please enter a valid tank. \n'))