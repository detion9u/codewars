def nearest_value(values: set, one: int) -> int:
    # your code here
    lis1 = list(values)
    if(len(lis1) == 1):
        return lis1[0]
    lis1.sort()
    if one < min(lis1):
        return lis1[0]
    elif one > max(lis1):
        return lis1[-1]    
    middle = lis1[len(lis1)//2]
    idx = lis1.index(middle)
    num1 = 1
    num2 = 1
    lisa = []
    lisb = []

    if middle > one:
        for it in lis1[:idx]:
            if(one - it) < 0:
                lisa.append(it - one)
            else:
                lisa.append(one - it)

        num1 = lis1[lisa.index(min(lisa))]
        return min(num1,middle)

    else:
        for it in lis1[idx:]:
            if(one - it) < 0:
                lisb.append(it - one)
            else:
                lisb.append(one - it)
        num2 = lis1[lisb.index(min(lisa))]
        return min(num2,middle)



if __name__ == "__main__":
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")