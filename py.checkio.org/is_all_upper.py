def is_all_upper(text: str) -> bool:
    sLar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    slow = 'abcdefghijklmnopqrstuvwxyz'
    sdigit = '1234567890'

    lis1 = list(text)
    #remove the repeated alpha
    lis1 = list(set(lis1))
    if lis1 == [] or lis1 == [''] or lis1 == [' ']:
        return True
    
    for it in lis1:
        if it in slow:
            return False
        elif  '' in lis1 and len(lis1) == 1 :
            return True
        elif it in sdigit:
            return True
        elif it in sLar:
            continue    
    return True
if __name__ == '__main__':
    print("Hello Python!")
    print(is_all_upper('ALL UPPER'))

    #These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")