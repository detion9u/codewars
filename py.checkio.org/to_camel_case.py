# to convert the name of a function (a string) from the Python format 
# (for example "my_function_name") into CamelCase ("MyFunctionName")
def to_camel_case(name: str) -> str:
    #replace this for solution
    str1 = ''
    for i in range(len(name)):
        if i == 0:
            str1 = str1 + name[i].upper()
        elif name[i] == '_':
            continue
        elif name[i - 1] == '_':
            str1 = str1 + name[i].upper()
        else:
            str1 = str1 + name[i]          
    return str1

if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
