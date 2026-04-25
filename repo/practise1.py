#Write a program which will find all such numbers 
# which are divisible by 7 but are not a multiple of 5,
#  between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.
num1=int(input("enter the range start: "))
num2=int(input("enter the range end: "))
def createList(num1,num2):
    newlist=[]
    for i in range (num1,num2+1):
        if i%5!=0 and i%7==0:
            newlist.append(i)
    print(newlist)
createList(num1,num2)