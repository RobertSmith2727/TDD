def check_pwd(password):
    if len(password) <= 7:
        return False

    if len(password) == 21:
        return False

    return True
