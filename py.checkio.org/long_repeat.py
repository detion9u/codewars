def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    # your code here
    dict1 = {}
    cnt = 1
    if line == '':
        return 0
    
    if len(line) == 1:
        return 1
    if len(line) == 2 and line[0] == line[1]:
        return 2
            
    for i in range(len(line)):
        if i == 0:
            dict1[line[i]] = 1  

        elif line[i-1] == line[i]:
                #dict1[line[i-1]] = dict1[line[i-1]] + 1
                cnt = cnt + 1
                if dict1[line[i]] < cnt:
                    dict1[line[i]] = cnt   
        else:
            if line[i] not in dict1.keys():
                dict1[line[i]] = 1
                cnt = 1
            
    #print(dict1)
    max1 = max(list(dict1.values()))
    return max1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert long_repeat('sdsffffse') == 4, "First"
    # assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    # assert long_repeat('abababaab') == 2, "Third"
    # assert long_repeat('') == 0, "Empty"
    assert long_repeat('aa') == 2, "Third"
    print('"Run" is good. How is "Check"?')