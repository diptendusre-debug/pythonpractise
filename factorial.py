def factorial(n):
    if n<0:
        print("Factorial is not posible as the number is in negetive range")
    elif n==0:
        print("Number is 0 and factorial is not possible")
    elif n==1:
        print("Factorial is 1 as the number is 1")
    else:
        print("The factorial of the number is")
        factorialValue=1
        for i in range(1,n+1,1):
            factorialValue*=i
        print(factorialValue)
number=int(input("Enter the number: "))
factorial(number)