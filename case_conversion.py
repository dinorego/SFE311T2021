import re
def decimalToBinary(n):
    # Convert Decimal number to Binary number
    return bin(n).replace("0b", "")
def chunks(array, n):
    # Divides up a string input into n equal chunks
    n = max(1, n)
    return (array[i:i+n] for i in range(0, len(array), n))
def convert_case(a,b):
    new_str = ""
    if len(a) > len(b):
        zipped_inputs = list(zip(a,b))
        for item in zipped_inputs:
            if str(item[0]) == '1':
                if item[1].islower():
                    new_str += item[1].upper()
                else:
                    new_str += item[1].lower()
            else:
                new_str += item[1]
            
    else:
        for i in range(len(a)):
            if a[i] == '1':
                if b[i].islower():
                    new_str += b[i].upper()
                else:
                    new_str += b[i].lower()
            else:
                new_str += b[i]
    return new_str

def merge(input_str, non_alphas):
    # place all non alphabets into a string
    for key in non_alphas.keys():
        val = non_alphas[key]
        input_str = input_str[:val] + key + input_str[val:]
    return input_str
def take_out_non_aphas(input_str):
    # take a string and get indexes of non-alphabets as a dictionary
    non_alphas = {}
    if input_str.isalpha():
        return non_alphas
    for i in range(len(input_str)):
        if not input_str[i].isalpha():
            non_alphas[input_str[i]] = i 
    return non_alphas

def swap(input_string, input_int):
    bin_input_int = str(decimalToBinary(input_int))
    non_alphas = take_out_non_aphas(input_string)
    input_string = re.sub("[^a-zA-Z]+", "", input_string)
    new_string = ""
    if (len(input_string) != len(bin_input_int)): 
        new_list = chunks(input_string,len(bin_input_int))
        for item in new_list:
            new_string += convert_case(bin_input_int, item)
    else:
        new_string = convert_case(bin_input_int, input_string)
    if len(non_alphas) > 0:
        new_string = merge(new_string, non_alphas)    
    return new_string


if __name__ == '__main__':  
    # few test cases, formal test in unit test file
    print(swap("absoluTE", 9))
    print(swap("absoluTE", 4))
    print(swap("absoluTE absoluTE", 9))
    print(swap("mine",11))
    print(swap("Mine",11))
    print(swap("no ways", 11))