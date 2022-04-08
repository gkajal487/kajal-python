import time
kajal=1+4j
if(type(kajal)==int):
    print("type if kajal is int")
elif(type(kajal)==float):
    print("type of kajal is float")
elif(type(kajal)==str):
    print("type of kajal is str")
elif(type(kajal)==bool):
    print("type of kajal is bool")
elif(type(kajal)==complex):
    print("type of kajal is complex")
elif(type(kajal)==list):
    print("type of kajal is tuple")
elif(type(kajal)==set):
    print("type of kajal is set")  
elif(type(kajal)==dict):
    print("type of kajal is dict") 
elif(type(kajal)==range):
    print('type of kajal is range') 
else:
    print("all data type are unknow")                
print()
time.sleep(2)
print('end of an application')