def frequency_sort(items):
    # your code here
    if len(items) <= 1:
        return items
    #lis1 = list(enumerate(items))
    
    lis1 = list(set(items))
    lis2 = []
    dict1 = {}
    tmp = 0
    #print("lis1",lis1)
    for it in lis1:
        dict1[it] = items.count(it)
        
    for j in range(1,len(lis1)):
        i = j - 1
        if items.count(lis1[i]) < items.count(lis1[j]):
            lis1[i],lis1[j] = lis1[j],lis1[i]
            continue
        elif items.count(lis1[i]) == items.count(lis1[j]):
            if items.index(lis1[i]) > items.index(lis1[j]):
                lis1[i],lis1[j] = lis1[j],lis1[i]
    
    #print(lis1)
    
    for i in lis1:
        cnt = dict1[i]
        while cnt > 0:
            lis2.append(i)
            cnt = cnt - 1

    #print(lis2)
    return lis2  




if __name__ == '__main__':
    print("Example:")
    #print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    #assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    # assert list(frequency_sort([])) == []
    # assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
