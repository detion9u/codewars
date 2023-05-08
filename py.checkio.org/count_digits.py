from unicodedata import digit


def count_digits(text: str) -> int:
    # your code here
    if text == '':
        return 0

    lis1 = text.split()
    lis2 = []
    lis3 = []
    lis4 = []
    cnt1 = 0
    myAlpha = '0123456789'
    for item in lis1:
        if item.isdigit():
            lis2.append(item)
        else:
            lis3.append(item)

    if len(lis2) == 0:
        cnt1 = 0
    else:
        for item in lis2:
            cnt1 = cnt1 + len(list(item))
    
    if len(lis3) > 0:
        for item in lis3:
            for it in item:
                if it in myAlpha:
                    lis4.append(it)

    # print(lis3)
    # print(lis2) 
    # print(lis4) 
    return cnt1+ len(lis4)


if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))

    #These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
      'painting by Danish artist Anna '
      'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
