#coding:utf-8
def most_frequent2(data:list)->str:
    char = ''
    dict1 = {}
    for k in set(data):
        dict1[k] = data.count(k)
        if dict1[k] == max(dict1.values()):
            char = k
    
    # for k in set(data):
    #     if dict1[k] == max(dict1.values()):
    #         char = k
    return char
if __name__ == '__main__':
    print("Hello Python!")
    lis1  = [
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]
    print(most_frequent2(lis1))