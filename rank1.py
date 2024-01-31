#New file for every br
#One main file to call all other files (index), can either use it as a library or a menu

#User input tank they are using
User_Tank_Rank1 = str(input('What tank are you in? \n'))

#Using set to store tank names, set is used becuase names can't be used twice and it is iterable
usaSet = ["M2A4", "M2" ,"LVT(A)(1)", "M13 MGMC"]
gerSet = ["PZ.III B", "PZ.III E", "PZ.II C", "PZ.II F", "Flakpanzer I", "Pz.34(t)", "15cm sIG 33 B Sfl"]
rusSet = ["BT-5"]
gbrSet = {""}
itaSet = {""}
sweSet = {""}
fraSet = {""}

usaSet.sort()
gerSet.sort()
rusSet.sort()

tank_list=(usaSet, gerSet, rusSet)
#this goes through the set and lists all tanks within
#for tanks in usaSet:
    #print(tanks)


#function that takes in User_Tank and compares it to the set we created, if a tank is found then the funciton will search and find other tanks at the same rank
if User_Tank_Rank1.upper() in usaSet:
    print('Other tanks at this rank')
elif User_Tank_Rank1.upper() in gerSet:
        print('Other tanks at this rank')
elif User_Tank_Rank1.upper() in rusSet:
            print('Other tanks at this rank')
else:
    str(input('Please enter a valid tank. \n'))
    





#function that scans the other sets and displays other tanks at this rank
if User_Tank_Rank1.upper() in usaSet:
    for tanks in gerSet, rusSet, gbrSet, itaSet, sweSet, fraSet:
        print(tanks)
elif User_Tank_Rank1.upper() in gerSet:
    for tanks in usaSet, rusSet, gbrSet, itaSet, sweSet, fraSet:
        print(tanks)
elif User_Tank_Rank1.upper() in rusSet:
    for tanks in usaSet, gerSet, gbrSet, itaSet, sweSet, fraSet:
        print(tanks)
