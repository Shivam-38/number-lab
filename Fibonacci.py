"""Taking User's input to obtain the fabonacci series"""
a = 0
b = 1

user = int(input("Enter Chocie(1 or 2): "))

if user == 1:

    count = 0
    n = int(input("Enter the no. of Terms you want: "))

    while count < n:
        print(a, end=" ")
        a , b = b , a + b
        count += 1