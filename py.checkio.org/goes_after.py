def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    if word == "":
        return False

    if first == second:
        return False

    if word.find(first) < 0 or word.find(second) < 0:
        return False
    
    if word.find(first) >= 0: 
        if word.index(first) + 1 < len(word):
            if word[word.index(first) + 1] == second:
                if word.find(second) < word.index(first):
                    return False
                    
                return True 
    else:
        return False  
    return False        
    


if __name__ == "__main__":
    print("Example:")
    print(goes_after("world", "w", "o"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after("almaz","m","a") == False
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after("transport", "r", "t") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
