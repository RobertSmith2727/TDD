def check_pwd(password):
    if len(password) <= 7 or len(password) >= 21:
        return False

    if password.isupper():
        return False

    return True
