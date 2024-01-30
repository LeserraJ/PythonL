#New file for every br
#One main file to call all other files (index), can either use it as a library or a menu

#User input tank they are using
User_Tank = str(input('What tank are you in? \n'))

#Using set to store tank names, set is used becuase names can't be used twice and it is iterable
usaSet = {"M2A4", "M2" , "LVT(A)(1)", "M13 MGMC"}
gerSet = {""}
rusSet = {""}
gbrSet = {""}
itaSet = {""}
sweSet = {""}
fraSet = {""}
#this goes through the set and lists all tanks within
#for tanks in usaSet:
    #print(tanks)


#function that takes in User_Tank and compares it to the set we created, if a tank is found then the funciton will search and find other tanks at the same rank
if User_Tank in usaSet:
    print('Valid tank, scanning for other tanks')
else:
    str(input('Please enter a valid tank. \n'))


#function that scans the other sets and displays other tanks at this rank
if User_Tank in usaSet:
    for tanks in gerSet, rusSet, gbrSet, itaSet, sweSet, fraSet:
        print(tanks)