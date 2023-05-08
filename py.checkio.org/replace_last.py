def replace_last(line: list) -> list:
    # your code here
    lis1 = []
    if line is [] or len(line) == 1:
        return line
    elif len(line) >= 2:
        it = line[len(line)-1]
        lis1.append(it) 
        lis1.extend(line[:-1]) 
        return lis1
   
      
if __name__ == '__main__':
    print("Example:")
    # print(replace_last([2, 3, 4, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    # assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([10,10]) == [10,10]
    # assert replace_last([1]) == [1]
    # assert replace_last([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
