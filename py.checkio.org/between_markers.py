def between_markers(text: str, begin: str, end: str) -> str:
    # mystr = text[text.index(begin) + 1:text.index(end)]
    idx1 = 0
    idx2 = 0
    if begin == '>' and end == '<':
        if text.count(begin) == 0 and text.count(end) == 0:
            return ''

    if text.count(begin) == 0 and text.count(end) == 0:
        return text

    if text.count(begin) == 0 and text.count(end) > 0:   
        return text[:text.index(end)] 

    if text.count(begin) > 0 and text.count(end) == 0:   
        return text[text.index(begin) + len(begin):]  

    if text.count(begin) > 0 and text.count(end) > 0:    
        return text[text.index(begin) + len(begin):text.index(end)]  

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    #These "asserts" are used for self-checking and not for 
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')