def is_acceptable_password(words):
    str1 = words
    my_digits = '0123456789'
    flag_digit = False
    flag_alpha = False
    if len(str1) > 9:
        return True

    if len(str1) <= 6:
        return False

    if len(str1) > 6 and len(str1) <= 9:
        for it in str1:
            if it in my_digits:
                flag_digit = True
            elif it.isalpha():
                flag_alpha = True

    if flag_digit == True and flag_alpha == True:
        return True
    else:
        return False    
                


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
