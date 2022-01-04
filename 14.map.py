def farenheit(T):
    return((float(9)/5) * T + 32)
def celcius(T):
    return ((float(5)/9)*(T - 32))

temperatures = (36.5, 37, 37.5, 38, 39)

F = map(farenheit, temperatures)
C = map(celcius, F)
temperatures_in_Farenheit = list(map(farenheit, temperatures))
temperatures_in_Celcius =list(map(celcius, temperatures_in_Farenheit))

print(temperatures_in_Farenheit)
print(temperatures_in_Celcius)

#with lambda

c = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)* x +32, C))
print(F)
C = (list(map(lambda x: (float(5)/9)* (x -32), F)))
print(C)