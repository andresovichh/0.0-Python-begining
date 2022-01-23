main, interest = input("Please, input main and yearly interest expected: ").split()

main = float(main)
interest = float(interest)

for i in range(1, 11):
    main = main + (main * (interest / 100))
    print ("Year {} capital + interest = {:.2f}".format(i, main))