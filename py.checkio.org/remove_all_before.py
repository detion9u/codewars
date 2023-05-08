#def remove_all_before(items: list, border: int) -> Iterable:
def remove_all_before(items: list, border: int):
    lis1 = []
    inx = 0
    if len(items) == 0:
        return items
    elif items.count(border) == 0:
        return items    
    else:
        #inx = items.index(border)
        lis1 = items[items.index(border):]
    return lis1
if __name__ == '__main__':
    print("Hello Python!")
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")