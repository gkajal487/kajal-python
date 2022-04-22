#Remove Duplicates from a list using the Temporary List

my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list)



#remove the list using for loop

my_list = [1,2,2,3,1,4,5,1,2,6]
myFinallist = []
for i in my_list:
    if i not in myFinallist:
       myFinallist.append(i)
print(list(myFinallist))


#using while loop

my_list = [1,2,2,3,1,4,5,1,2,6]
myFinallist = []
while i in my_list:
    if i not in myFinallist:
       myFinallist.append(i)
print(list(myFinallist))



