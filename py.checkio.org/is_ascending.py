from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    # your code here
    tmp = 0
    flag = False

    if items == []:
        return True

    if len(items) == 1:
        return True    
    
    tmp = items[0]
    for i in range(1,len(items)):
        if tmp < items[i]:
            flag = True
            tmp = items[i]
        else:
            return False    
       
    return flag


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
