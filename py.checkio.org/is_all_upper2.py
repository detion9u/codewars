def is_all_upper(text: str) -> bool:
    # your code here
    str_alpha = 'abcdefghijklmnopqrstuvwxyz'
    flag = True
    flag_alphp = False
 
    if len(text) == 0:
        return False
    
    for t in text:
        if t in str_alpha:
            flag = False
        elif t.isalpha():
            flag_alphp = True       
    return flag & flag_alphp

if __name__ == "__main__":
    print("Example:")
    print(is_all_upper("ALL UPPER"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")