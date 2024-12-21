import re

def valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

email = input("enter an email address to validate: ")
result = valid_email(email)
print("Valid Email Address:", result)
