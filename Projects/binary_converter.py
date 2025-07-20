print("Int to Binary Converter")
print("Ctrl + C to Exit")
while 1 == 1:
    NUM = int(input("Enter the Number : "))
    d = NUM
    binary = " "
    while d >= 1:
        r = d % 2
        d = d // 2
        binary = str(r) + binary
    print("The Binary value for " + str(NUM) + " is : " + binary)
