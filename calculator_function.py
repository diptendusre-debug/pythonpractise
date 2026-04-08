firstNumber=int(input("Enter the first Number : "))
secondNumber=int(input("Enter the Second Number : "))
operation =str(input("Enter the operation you want to perfrom i.e Sum,Sub,Mul,Div : "))
def addition(x,y):
    sum= x+y
    print("The sum is :"+ str(sum))

def substraction(x,y):
    if x>y:
        sub=x-y
        print("The substraction is "+ str(sub))
    else:
        sub=y-x
        print("The substraction is " +str(sub))

def multiplication(x,y):
    mul=x*y
    print("The multiplication is "+str(mul))

def division(x,y):
    if x>y:
        div=x/y
        print("The division is "+str(div))
    else:
        div=y/x
        print("The division is "+str(div))


if operation=="Sum":
    addition(firstNumber,secondNumber)
elif operation=="Sub":
    substraction(firstNumber,secondNumber)
elif operation=="Mul":
    multiplication(firstNumber,secondNumber)
elif operation=="Div":
    division(firstNumber,secondNumber)
else:
    print("No suitable Operation found")