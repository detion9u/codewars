#coding:utf-8
from unicodedata import digit


def high_and_low(numbers):
    # ...
    lis = []
    lis = list(numbers.split(' '))
    max1 = int(lis[0])
    min1 = int(lis[0])
    max_idx = 0
    min_idx = 0

    result1 = ''
    for i in lis:
        if max1 < int(i):
            max1 = int(i)
            max_idx = lis.index(i)
        if min1 > int(i):
            min1 = int(i)
            min_idx = lis.index(i)
    print(max1,lis[max_idx])
    print(min1,lis[min_idx])       
    result1 = str(max1) + ' ' + str(min1)
    
    return result1
    #return numbers
if __name__ == "__main__":
    print('Hello PYthon!')
    #assert(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")
    high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
