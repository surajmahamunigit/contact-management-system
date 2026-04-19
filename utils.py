def is_valid_name(name:str):
    return bool(name.strip())

def is_valid_phone(phone:str):
    return phone.isdigit() and len(phone)>=5

def is_valid_email(email:str):
    return '@' in email and '.com' in email