from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    # your code here
    tmp = ''
    lis_front = []
    lis2 = []
    lis_tail = []
    for i in range(len(files)):
        
        #if len(files[files[i].rindex(files[i][0])+1:]) > 0  and files[i].count('.')  > 1 :
        # if files[i].count('.')  > 1 :
        #     lis1.append(files[i])
        if files[i][0] == '.' and files[i].count('.') < 2:
            lis_front.append(files[i])    
        elif files[i][-1] == '.':   
            lis_front.append(files[i])    
        else:
            lis2.append(files[i])    
        # elif files[i] > files[j]:
        #     files[i], files[j] = files[i], files[j]
    
    #tmp = lis2[0]

    for i in range(1,len(lis2)):
        for j in range(len(lis2)-1):
            if lis2[i][lis2[i].rindex('.') + 1:] < lis2[j][lis2[j].rindex('.') + 1:]:
                lis2[i], lis2[j] = lis2[j], lis2[i]
            elif lis2[i][lis2[i].rindex('.') + 1:] == lis2[j][lis2[j].rindex('.') + 1:]:
                #if lis2[i][:lis2[i].rindex('.')] > lis2[j][:lis2[j].rindex('.')]:  
                if lis2[i][:lis2[i].rindex('.')] < lis2[j][:lis2[j].rindex('.')]:
                    lis2[i], lis2[j] = lis2[j], lis2[i]
            else:
                continue

    # for i in range(1,len(lis2)):
    #     j = i - 1
    #     if lis2[i][lis2[i].rindex('.') + 1:] == lis2[j][lis2[j].rindex('.') + 1:]:  
    #         if lis2[i][:lis2[i].rindex('.')] < lis2[j][:lis2[j].rindex('.')]:
    #             lis2[i], lis2[j] = lis2[j], lis2[i]

    if len(lis_front) > 0:
        lis_front.sort()
        lis_front.extend(lis2) 
        return lis_front

    if len(lis_tail) > 0:
        lis_tail.sort()
        lis2.extend(lis_tail)    
        return lis2

    #lis1.extend(lis2)    
    # print(lis2)
    # print(lis1)

    return lis2


if __name__ == '__main__':
    print("Example:")
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    #These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(["1.cad","2.bat","1.aa","1.bat"]) == ["1.aa","1.bat","2.bat","1.cad"]
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
