def char_counter():
    result = ""
    output = dict()
    text = input("enter the text : ")
    for i in text :
        if i.isalpha():
            result += i
    for j in result:
        if j not in output.keys():
            output.update({j: 1})
        else :
            output[j] += 1

    return print(output)

char_counter()