import random
import math
'''
generate random list of a random list random values inside a list
5 values 

1 to 9
list
for loop
random numbers between 1 and 9
'''


randomm = []

for i in range(5):
    randomm.append(random.randrange(1,10))
for i in randomm:
    print(i) 
