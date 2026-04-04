
import re
text = """
Contact us at support@gmail.com or sales@yahoo.in.
Invalid emails: test@.com, user@com, @gmail.com
Also valid: john.doe123@company.co.uk
"""

# Regular expression pattern for validating email addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
result = re.findall(pattern, text)

print(result)

newtext="Diptendu Bandyopadhyay"
pattern1=r"i"
result1=re.sub(pattern1,"e",newtext)
print(result1)