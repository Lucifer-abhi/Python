a=int(input("Enter the lower limit of range: "))
b=int(input("Enter the upper limit of range: "))
isPrimeNumber=True
for j in range(a, b+1):
    for i in range(2,j):
        if j%i==0:
            isPrimeNumber= False
            break
    if isPrimeNumber==True:
        print(j,"is a prime number")
    else:
        print(j,"is not a prime number")