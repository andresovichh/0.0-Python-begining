num1, operator, num2 = input("Please, input two values: ").split()

num1 =  int(num1)
num2 =  int(num2)

sum = num1 + num2

difference = num1 - num2

product = num1 * num2

remanider = num1 % num2

quotient = num1 / num2

# print the results
if operator == "+":
    print("{} + {} = {}".format(num1, num2, sum))
elif operator is "-":
    print("{} - {} = {}".format(num1, num2, difference))
elif operator is "*":
    print("{} * {} = {}".format(num1, num2, product))
elif operator is "/":
    print("{} / {} = {}".format(num1, num2, quotient))
elif operator is "%":
    print("{} % {} = {}".format(num1, num2, remanider))
else:
    print("Not recognizable")