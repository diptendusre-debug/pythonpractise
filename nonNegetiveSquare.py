#The provided code stub reads an integer, , from STDIN. For all non-negative integers ,i<n print n2
num=int(input("Enter the number : "))

def nonNegetiveIntegers(num):
    if num<=0:
        print("no solution")
    else :
        for i in range (num):
            print(i**2)

nonNegetiveIntegers(num)
    
    