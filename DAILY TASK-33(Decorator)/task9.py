import time 
def Test_Case1(func):
    def inner(fname,lname,username,p1,p2,email):
        if(username=="rahul12345" and p1=="12345"):
            print("---Username & Passwoord---")
            print(username,p1)
            print("---------------")
        else:
            func(fname,lname,username,p1,p2,email)
    return inner
@Test_Case1
def New_User_Case1(fname,lname,username,p1,p2,email):
    print("----New User Information----")
    print(fname,lname,username,p1,p2,email)
    print("---------------------------------")
New_User_Case1("Rahul","Reddy","rahul12345","12345","12345","rahul@gmail.com")
print()
time.sleep(2)
print("end of an application")

