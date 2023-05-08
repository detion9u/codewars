from asyncio import current_task


def is_majority(items: list) -> bool:
    # your code here
    c_t = 0
    c_f = 0
    
    if items is []:
        return False

    c_t = items.count(True)
    c_f = items.count(False)

    if c_t == c_f:
        return False
    
    if c_t > c_f:
        return True
    else:
        return False

    
if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")