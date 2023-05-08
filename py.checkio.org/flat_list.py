def flat_list(array):
    str1 = str(array)
    result = ''
    lis1 = []
    lis2 = []
    for it in str1:
        if it =='[' or it ==']':
            pass
        else:
            result = result + it

    #result = '[' + result + ']' 
    result = result.strip(' ')
    result = result.strip(',')
    lis1 = result.split(', ')
    print(lis1)   

    for it in lis1:
        lis2.append(int(it.strip()))
    
    # print(lis2)
    return lis2    
    # for it in array:
    #     if it =='[' or it ==']' or it == ',' or it == ' ':
    #         pass
    #     elif type(it) is list:
    #         for i in it:
    #             if i =='[' or i ==']' or i == ',' or i == ' ':
    #                 pass
    #             elif type(i) is list:   
    #                 for ie in i:
    #                     if ie =='[' or ie ==']' or ie == ',' or ie == ' ':
    #                         pass
    #                     elif type(ie) is list:   
    #                         for iee in ie:
    #                             if iee =='[' or iee ==']' or iee == ',' or iee == ' ':
    #                                 pass
    #                             else:
    #                                 lis2.append(iee)
    #                     else:
    #                         lis2.append(ie)
    #             else:
    #                 lis2.append(i)
    #     else:
    #         lis2.append(it)

    # result = '[' + result + ']' 
    #print(lis2)
    
    #return lis2 [-1,[1,[-2,[3],[[5],[10,-11],[1,100,[-1000,[5000]]],[20,-10,[[[]]]]]]]]

if __name__ == '__main__':
    flat_list([-1,[1,[-2,[3],[[5],[10,-11],[1,100,[-1000,[5000]]],[20,-10,[[[]]]]]]]])
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')