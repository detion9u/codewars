def count_words(text: str, words: set) -> int:
    words1 = [it for it in words]
    
    dict1 = dict.fromkeys(words)

    for k in dict1.keys():
        dict1[k] = text.lower().count(k)
    
    result = len(dict1.keys())
    cnt = 0 
    for k,v in dict1.items():
        if v == 0:
            cnt = cnt + 1
    if cnt > 0:
        result = result - cnt
        return result

    return result
    
   
if __name__ == '__main__':
    print("Example:")
    # print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
