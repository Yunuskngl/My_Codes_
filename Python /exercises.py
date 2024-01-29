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

#is perfect numbers

"""
import numpy as np

def divisors(num):
    arr = np.array([1])
    for i in range(2,num):
        if num%i == 0 : arr = np.append(arr,i)
       
        
    return arr



a = int(input("input a number:"))
result = divisors(a)
print(result)
sum = 0
for i in range(0,len(result)):
    sum += result[i]

if sum == a : print("this is perfect number")
else : print("this is not perfect number")
"""
#--------------------------------------------------------

#Between 1-1000 of perfect numbers

"""
import numpy as np

def is_perfect(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0 : sum+=i
    
    if sum != num : return False
    return True
    
        
for i in range(0,1000):
    if(is_perfect(i) == True) : print(i) 
"""
#--------------------------------------------------------

#find random number
"""
import random
import time

num = random.randint(1,40)
predict = 7

while True : 
    prenum = int(input("input number:"))
    
    if (prenum < num) : 
        print("please predict more than bigger number")
        predict = predict - 1
        time.sleep(1)
    elif (prenum > num) : 
        print("please predict more than lower number")
        predict = predict - 1
        time.sleep(1)
    else :
        time.sleep(2)
        print("success")
        break
    if predict == 0 : 
        print("fail")
        break 
    
"""
        
#--------------------------------------------------------


