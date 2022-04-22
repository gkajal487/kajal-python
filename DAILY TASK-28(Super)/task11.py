import time
class india:
    def capital (self):
        print("new delhi")
    def language (self):
        print("hindi,english")
class USA:
    def capital(self):
        print("washington")
    def language(self):
      print("english")
obj_ind = india()
obj_usa = USA()
for a in (obj_ind, obj_usa):
  a.capital()
  a.language()
print()
time.sleep(2)
print("end of an appliation")