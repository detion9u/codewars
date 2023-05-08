def reverse_roman(roman_string):
    dict1 = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    num1 = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_string[i-1] == 'I' and roman_string[i] == 'V':
            num1 = num1 - 1*2  # 4
        elif i > 0 and roman_string[i-1] == 'I' and roman_string[i] == 'X':
            num1 = num1 - 1*2  # 9  
        elif i > 0 and roman_string[i-1] == 'X' and roman_string[i] == 'L':
            num1 = num1 - 10*2  # 40
        elif i > 0 and roman_string[i-1] == 'X' and roman_string[i] == 'C':
            num1 = num1 - 10*2   # 90     
        elif i > 0 and roman_string[i-1] == 'C' and roman_string[i] == 'D':
            num1 = num1 - 100*2  # 400 
        elif i > 0 and roman_string[i-1] == 'C' and roman_string[i] == 'M':
            num1 = num1 - 100*2   # 900        
        
        num1 = num1 + dict1[roman_string[i]]
    return num1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert reverse_roman('VI') == 6, '6'
    # assert reverse_roman('LXXVI') == 76, '76'
    # assert reverse_roman('CDXCIX') == 499, '499'
    #assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    assert reverse_roman('MX') == 1010, '1010'
    # print('Great! It is time to Check your code!');