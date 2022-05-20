import time
def test_sqare_case1(num):
    return num**num
assert test_sqare_case1(3)==9,"the square of 3 is 9"
assert test_sqare_case1(5)==25,"the sqare of 5 is 25"
assert test_sqare_case1(10)==100,"the square of 10 is 100"
print(test_sqare_case1(3))
print()
print(test_sqare_case1(5))
print()
print(test_sqare_case1(10))
print()
time.sleep(2)
print("end of an aaplication")