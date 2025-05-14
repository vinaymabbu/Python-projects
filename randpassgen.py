# collect the user preference
# length
# should contain uppercase
# should contain special
# shold contain digits
# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of the each character type
# ensure the length is valid

import random
import string

def generate_password():
    length=int(input("enter the desired password length :").strip())
    include_uppercase=input("include uppercase letters ?(yes/no)").strip().lower()
    include_specialchars=input("include special characters ?(yes/no)").strip().lower()
    include_numbers=input("include numbers ?(yes/no)").strip().lower()
    if length<4:
        print("enter valid length")
        return
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase if include_uppercase=="yes" else ""
    digits=string.digits if include_numbers=="yes" else ""
    special=string.punctuation if include_specialchars=="yes" else ""
    all_characters=lower+upper+digits+special

    required_characters=[]
    if include_uppercase=="yes":
        required_characters.append(random.choice(upper))
    if include_specialchars=="yes":
        required_characters.append(random.choice(special))
    if include_numbers=="yes":
        required_characters.append(random.choice(digits))
    
    remaining_length=length-len(required_characters)
    password=required_characters

    for _ in range(remaining_length):
        character=random.choice(all_characters)
        password.append(character)
        random.shuffle(password)
    

    str_password="".join(password)
    return str_password




password=generate_password()
print(password)