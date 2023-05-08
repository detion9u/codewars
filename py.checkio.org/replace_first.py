from typing import Iterable


def replace_first(items: list) -> Iterable:
    if [] == items or len(items) == 1:
        return items
    
    lis = items[1:]    
    lis.append(items[0])
    return lis

if __name__ == '__main__':
    print("Hello Python!")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")