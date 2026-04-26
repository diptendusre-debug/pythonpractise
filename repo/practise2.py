#Check if password if strng 
#password should be more than  8 character 
#password should contain digits
#password should contain alpha numeric character
import re
password=str(input("Enter the password : "))

def contains_digit(password):
    for i in  password:
        if i.isdigit():
            return True
            break
    return False
def contains_alphanum(password):
    for i in password:
        if i.isalnum():
            return True
            break
    return False

def isPasswordStrong(password):
    if len(password)>=8:
        if contains_digit(password):
            if contains_alphanum(password):
                print("Password is strong")
    else:
        print("Password is not strong")

isPasswordStrong(password)
        

