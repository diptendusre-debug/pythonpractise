# check email address if it is valid or not 
'''
Pseudocode
input the email address
declare function (email)
create a pattern 
match the patter
if true return valid
else false 
'''
import re
emailid=input("Enter the email id :")
def validateEmail(emailid):
    pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if (re.match(pattern,emailid)):
        print("Email id is valid")
        return True
        
    else:
        print("Email id is false")
        return False
        
validateEmail(emailid)
