import string

def check_password_strength(password):
    score = 0
    
    password_set = set(password)

    lc = set(string.ascii_lowercase)
    uc = set(string.ascii_uppercase)
    digits = set(string.digits)
    punctuation = set(string.punctuation)

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 2

    if password_set & lc:
        score += 1
    if password_set & uc:
        score += 1
    if password_set & digits:
        score += 1
    if password_set & punctuation:
        score += 1

    return score
print(check_password_strength("Football@123"))