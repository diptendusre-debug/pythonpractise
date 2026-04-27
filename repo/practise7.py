'''
Define a class which has at least two methods: getString: to get a string from console input printString: 
to print the string in upper case. 
Also please include simple test function to test the class methods.
'''
'''
input the string
create class
convert the string into upper case

'''
myString=input("Enter the String : ")
class PrintString:
    def __init__(self,myString):
        self.string=myString
    def printString(self):
        print(self.string)
        print(self.string.upper())
myString1=PrintString(myString)
myString1.printString()
