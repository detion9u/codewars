def max_digit(number: int) -> int:
    # your code here
    if number < 10:
        return number
    lis1 = list(set(list(str(number))))
    
    return int(max(lis1))

if __name__ == '__main__':
    print("Hello Python!")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")