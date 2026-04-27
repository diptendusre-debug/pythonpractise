'''
Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a 
list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 
Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
'''
'''
Psudocode
input the numbers
create function for list
return tuple

create function for tuple 
return list

'''

numbers=(input("Enter the numbers:"))
print(numbers)

def createList(numbers):
    newlist=numbers.split(",")
    print(newlist)
    newTuple=tuple(newlist)
    print(newTuple)

createList(numbers)