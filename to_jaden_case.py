#coding:utf-8
def to_jaden_case(string):
    lis = string.split()
    lis2 = []
    listmp = []
    str2 = str()
    for i in range(len(lis)):
      
        k =lis[i][0].upper()
        #divide the first alhpa,
        listmp = list(lis[i][1:])
        str3 = k
        for it in listmp:
            str3 += ''.join(it)
    
        lis2.append(str3)

    for i in lis2:    
        str2 += ' ' + i
    str2 = str2[1:]
    print(lis2) 
    print(str2)
    
    

if __name__ == "__main__":
    print('Hello PYthon!')
    str1 = "How can mirrors be real if our eyes aren't real"
    str3 = to_jaden_case(str1)
    print(str3)