principal = input("Enter principal: ")

principal = float(principal)

interest = input("Enter interest: ")
interest = float(interest)



for i in range (10):
    principal = principal + (principal * (interest * .01))

print("{:.2f}".format(principal))
