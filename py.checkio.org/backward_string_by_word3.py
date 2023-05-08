def backward_string_by_word(text: str) -> str:
    # your code here
    if text == '':
        return text
        
    in_stack = []
    char1 = ''
    char2 = ''
    

    for i in range(len(text)):
        if not text[i].isspace():
            in_stack.append(text[i]) 
        elif text[i].isspace():
            if len(in_stack) > 0:
                for t in in_stack[::-1]:
                    char1 = char1 + ''.join(t)
            
                char2 = char2 + char1
                char2 = char2 + text[i]
                
                char1 = ''
                in_stack = []
            else:
                char2 = char2 + text[i]

    if len(in_stack) > 0:
        for t in in_stack[::-1]:
            char1 = char1 + ''.join(t)
    
    char2 = char2 + char1

    #print(char2)        
    return char2

            
    
      
    
if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   a world') == 'olleh   a dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
