from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:
    # your code here
    x = 0
    y = 0
    for it in instructions:
        if it == 'f':
            y = y + 1

        if it == 'b':
            y = y - 1    

        if it == 'l':
           x = x - 1

        if it == 'r':
           x = x + 1   
    #print(x, y)       
    return (x, y)

if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
