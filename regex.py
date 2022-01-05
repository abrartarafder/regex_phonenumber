import re

def validate_phone(value):
    ip = input("Enter a phone number: ")

    phone_regex = re.compile('[+0-9]*(-)*[(]*[0-9]{3}[)]*(-)*[0-9]{3}(-)*[0-9]{4}')
    phone_match = phone_regex.match(ip)
    if phone_match:
        return "VALID PHONE NUMBER"
    else: 
        return "INVALID PHONE NUMBER"
