import random
import math
# ---------- PROBLEM : CREATE A RANDOM LIST ----------
# Generate a random list of 5 values between 1 and 9
numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))
 
numList.sort()

numList.reverse()

numList.pop(:2)

for k in numList:
    print(k, end=", ")
print()