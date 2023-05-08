# to convert the name of a function (a string) from CamelCase ("MyFunctionName") 
# into the Python format ("my_function_name") 
def from_camel_case(name: str) -> str:
    #replace this for solution
    str1 = ''
    for it in name:
        if it == name[0]:
            str1 = str1 + it.lower()
        elif it.isupper():
            str1 = str1 + '_' + it.lower()
        else:
            str1 = str1 + it    

    #print(str1)
    return str1

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")