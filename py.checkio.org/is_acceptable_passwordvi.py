def is_acceptable_password(words):
    str_d = '0123456789'
    str_a = 'abcdefghijklmnopqrstuvwsyz'
    flag_digit = False
    flag_alpha = False
    if len(set(words.lower())) < 3:
        return False 
        
    if len(words) <= 6:
       return False
    
    if words.lower().count('password') > 0:
        return False

    if len(words) > 6 and len(words) <= 9:
        for it in words.lower():
            if it.isdigit():
                flag_digit = True  
            elif it.isalpha():
                flag_alpha = True

        return flag_alpha & flag_digit         
    
    if len(words) > 9:
        return True
        
    

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_acceptable_password("short") == False
    # assert is_acceptable_password("short54") == True
    # assert is_acceptable_password("muchlonger") == True
    # assert is_acceptable_password("ashort") == False
    # assert is_acceptable_password("muchlonger5") == True
    # assert is_acceptable_password("sh5") == False
    # assert is_acceptable_password("1234567") == False
    # assert is_acceptable_password("12345678910") == True
    # assert is_acceptable_password("password12345") == False
    # assert is_acceptable_password("PASSWORD12345") == False
    # assert is_acceptable_password("pass1234word") == True
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
