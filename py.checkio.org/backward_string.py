from sqlalchemy import null


def backward_string(val: str) -> str:
    str1 = ''
    lis1 = list(val)
    lis1.reverse()
    str1 = str1.join(lis1)

    #print(str1)
    #print(lis1)
    return str1
    

if __name__ == '__main__':
    print("Hello Python!")
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'