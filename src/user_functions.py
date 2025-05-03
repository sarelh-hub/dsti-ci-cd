import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Za-z]", password):  # au moins une lettre
        return False
    if not re.search(r"\d", password):        # au moins un chiffre
        return False
    if not re.search(r"[^\w\s]", password):   # au moins un caractère spécial (non lettre, non chiffre, non espace)
        return False
    return True



def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email
    
def get_user_name_from_input():
    """ Not empty string. No spaces. """
    user_name =  input("Create your user name: ")
    if (len(user_name) == 0 or " " in user_name or len(user_name) > 21):
        print("User Name is not valid.")
    else:
        return user_name

def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    password =  input("Create your password: ")
    if not is_valid_password(password):
        print("Password needs to be at least 8 characters long with at least one number, one special character and one letter.")
    else:
        return password
