def check_pwd(password):
    if len(password) <= 7 or len(password) >= 21:
        return False

    if not any(element.islower() for element in password):
        return False

    if not any(element.isupper() for element in password):
        return False

    if not password.isnumeric() and password.isalpha():
        return False

    return True
