def check_pwd(password):

    if len(password) <= 7 or len(password) >= 21:
        return False

    if not any(element.islower() for element in password):
        return False

    if not any(element.isupper() for element in password):
        return False

    if not any(element.isnumeric() for element in password):
        return False

    symbols = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_",
               "+", "-", "="]

    if not any(element in symbols for element in password):
        return False

    return True
