import math

def calculate_area(str, num1, num2=0):
    if str == "t":
        return 0.5 * num1 * num2
    
    elif str == "r":
        if num2 == 0:
            return num1 * num1
        else:
            return num1 * num2
    elif str == "c":
        return math.pi * num1 ** 2

print(calculate_area("t", 10, 7))
print(calculate_area("r", 10, 7))
print(calculate_area("r", 10))
print(calculate_area("c", 10))