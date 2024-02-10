def check_pwd(password):
    if len(password) <= 7 or len(password) >= 21:
        return False

    if not any(element.islower() for element in password):
        return False

    return True
