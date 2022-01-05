# re imported for regexpression
import re

# function to check phone number
def validate_phone():
    ip = input("Enter a phone number: ")
#     regex checker
    phone_regex = re.compile('^([+])?([0-9])?(-)?[(]?[0-9]{3}[)]?(-)?[0-9]{3}(-)?[0-9]{4}$')
#     checking match
    phone_match = phone_regex.match(ip)
   
    if phone_match:
        return "VALID PHONE NUMBER"
    else: 
        return "INVALID PHONE NUMBER"
    
print(validate_phone())
