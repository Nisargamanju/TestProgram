goodies = []

def StoreGoodies():
    n = int(input("Enter number of goodies: "))
    for i in range(n):
        goodie = input("\nGoodie Name: ")
        price = int(input("price: "))
        goodies.append([goodie, price])

    for i in range(n):
        for j in range(n):
            if goodies[i][1] < goodies[j][1]:
                temp = goodies[i]
                goodies[i] = goodies[j]
                goodies[j] = temp

def ShowGoodies(n_goodies):
    for goodie in goodies[:n_goodies]:
        print(goodie[0] + ": " + str(goodie[1]))

    print("And the difference between the chosen goodie with highest price and the lowest price is " + str(goodies[n_goodies - 1][1] - goodies[0][1]))


StoreGoodies()
n_employee = int(input("\n\nNumber of employee: "))
ShowGoodies(n_employee)
