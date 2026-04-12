def is_password_good(password):
    if len(password) < 8:
        return False
    
    has_digit = False
    has_lower = False
    has_upper = False
    
    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
    
    return has_digit and has_lower and has_upper