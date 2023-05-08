def unique_in_order(iterable):
    lis1 = []
    char1 = ''
    if type(iterable) is list:
        lis1 = list(set(iterable))
        return lis1
    if type(iterable) is str:
        char1 = iterable[0]
        lis1.append(char1)
        for i in range(len(iterable)):
           if char1 == iterable[i]:
               continue
           else:
               char1 = iterable[i]
               lis1.append(iterable[i])    
        return lis1   
if __name__ == '__main__':
    print('Hello!')
    unique_in_order('AAAABBBCCDAABBB')