#holoalphabetic sentence for a given alphabet is a sentence 
# using every letter of the alphabet at least once
def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    # your code here
    dict1 = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0
        }
    if len(text) < 26:
        return False

    for it in text.lower():
        if it in dict1.keys():
            dict1[it] = dict1[it] + 1   

    if min(dict1.values()) == 0:
        return False
    else:
        return True    

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')