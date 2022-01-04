a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

d = list(map(lambda x, y, z: y+z, a, b, c))
print(d)