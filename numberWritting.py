'''
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
12345..n
Note that "" represents the consecutive values in between.'''

num=int(input())
def printNum(num):
    if num<=0:
        print("No Solution")
    else:
        for i in range (1,num+1):
            print(i, end='')
printNum(num)