#Check if any string is palindrome or not 

myString=input("Enter the string : ")

def isPalindrome(myString):
    newString=myString[::-1]
    print(newString)
    if (newString==myString):
        return True
    else:
        return False
print(isPalindrome(myString))


def newPalindrome(myString):
    newString=""
    for i in myString[::-1]:
        newString=newString+i
    print(newString)
    if newString==myString:
        return True
    else: 
        return False
print(newPalindrome(myString))