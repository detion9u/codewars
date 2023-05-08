def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    a = text
    b = a.split()
    
    b = [it.replace('.','#') for it in b]
    b = [it.replace(',','#') for it in b]
    c = []
    lis = []
    for it in b:
        if it.count('#') > 0:
            lis.append(it[:it.index('#')])
            continue
        else:
            lis.append(it)
    b = lis
    lis = []
    for it in b:
        if it == '':
            continue
        else:
            lis.append(it)
    b = lis    
    #print(b)
    for i in range(len(b)):
        #print((b[i]))
        if b[i][0].isalpha() and b[i][-1].isalpha():
            #print(b[i],b[i][0],b[i][-1])
            c.append(b[i])
        else:
            continue    

    #print(c)        
    return c[0]


if __name__ == '__main__':
    print("Example:")
    # print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")