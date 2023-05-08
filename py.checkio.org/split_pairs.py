def split_pairs(a):
    # your code here
    lis1 = []

    if a == '':
        return []
    if len(a) % 2 == 1:
        a = a + '_'    
    lisa = list(range(0,len(a),2))
    lisb = list(range(1,len(a),2)) 
    #lis1 = list(map(lambda x,y: x+y,['a','b','c'],['b','_']))
    lis1 = lis1 = list(map(lambda x,y: x+y,[a[i] for i in lisa],[a[k] for k in lisb]))
   
    return lis1

if __name__ == '__main__':
    print("Hello Python!")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")