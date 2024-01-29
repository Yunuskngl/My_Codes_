#is prime number
"""
def is_asal(a):
    if (a <= 0): return False
    if (a == 1): return False
    if (a == 2): return True
    for i in range(2, a):
        if (a % i == 0): return False
    return True

while True:
    a = int(input("input a number: "))
    if (is_asal(a)):
        print(a, "is a prime number")
    else:
        print(a, "is not a prime number")

"""
#--------------------------------------------------------

#find divisors of a number

"""

import numpy as np

def divisors(num):
    arr = np.array([1])
    for i in range(2, num):
        if num % i == 0:
            arr = np.append(arr, i)
    
    return arr

a = int(input("input a number: "))
result = divisors(a)
print(result)



"""


#--------------------------------------------------------

