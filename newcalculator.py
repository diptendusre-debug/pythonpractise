number1=float(input("Enter the first Number :"))
number2=float(input("Enter the second Number: "))
operation=input(" Enter the operation you want to perform(+,_,*,/,%) :")
if operation=="+":
    sum=number1+number2
    print("The sum is : "+str(sum))
elif operation=="-":
    differance=number1-number2
    print("The difference is :" +str(differance))
elif operation=="*":
    product=number1*number2
    print("The product is : "+str(product))
elif operation=="/":
    quotient=number1/number2
    print("The quotient is : "+str(quotient))
elif operation=="%":
    remainder=number1%number2
    print("The remainder is : "+str(remainder))