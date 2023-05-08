MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code):
    # replace this for solution
    lis1 = []
    lis2 = []
    lis3 = []
    char = ''
    char1 = ''
    char3 = ''
    if code.count('   '):
        lis1 = code.split('   ')
        for item in lis1:
            lis3 = item.split()
            for el in lis3:
                char = char + ' '.join(MORSE[el])
            char = char + ' '
            lis2.append(char)
        char1 = char.strip(' ')
        # if char1[-1] == ' ':
        #     char1 = char1[:-1]    
        #return lis2[1][:-1]    
        #return char1[0].upper()
        #return char1[0].replace(char1[0],char1[0].upper())
        char3 = char1[0].upper()
        char3 = char3 + char1[1:]
        return char3
    else:
        lis1 = code.split()

        for item in lis1:
            char = char + ' '.join(MORSE[item])
        char1 = char.strip(' ')
        lis2.append(char) 
        #print(char1)
        #return lis2[0]
        #return char1[0].upper()
        #return char1[0].replace(char1[0],char1[0].upper())
        char3 = char1[0].upper()
        char3 = char3 + char1[1:]
        return char3


if __name__ == "__main__":
    print("Example:")
    print(morse_decoder("... --- ..."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    # assert morse_decoder("..--- ----- .---- ---..") == "2018"
    # assert (
    #     morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")
    #     == "It was a good day"
    # )
    print("Coding complete? Click 'Check' to earn cool rewards!")