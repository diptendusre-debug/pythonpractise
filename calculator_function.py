firstNumber=int(input("Enter the first Number : "))
secondNumber=int(input("Enter the Second Number : "))
operation =str(input("Enter the operation you want to perfrom i.e Sum,Sub,Mul,Div : "))
def addition():
    sum= firstNumber+secondNumber
    print("The sum is :"+ str(sum))

if operation=="Sum":
    addition()
