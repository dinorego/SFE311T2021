def expanded_form(input_int):
    input_str = str(input_int)
    str_length = len(input_str)
    expanded = ""
    for i in range(len(input_str)):
        if input_str[i] is not "0":
            expanded += input_str[i] + "0"*(len(input_str) -1 - i)
            if i <  len(input_str) -1:
                expanded += " + "
        
    if input_str == "0":
        expanded = "0"        
    if expanded.strip()[-1] == "+":
        expanded = expanded.strip()[:len(expanded.strip())-1]
    return expanded.strip()

if __name__ == '__main__':  
    # few test cases, formal test in unit test file
    print(expanded_form(10000))
    print(expanded_form(10001))
    #print(expanded_form(5))
    #print(expanded_form(68))
    #print(expanded_form(5934))
    
