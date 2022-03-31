#hetrogenious object are allowed

import time
l1=eval(input('enter the list data type:'))
print(l1)
print(type(l1))
print()
print("...fetching the data...")
for r in l1:
    time.sleep(1)
    print(r)
    time.sleep(2)
print("end of an application")

#output
#('rohit',150000,'kajal',35000,'market')
#('rohit', 150000, 'kajal', 35000, 'market')
#<class 'tuple'>

#...fetching the data...
#rohit
#150000
#kajal
#35000
#market
#end of an application
