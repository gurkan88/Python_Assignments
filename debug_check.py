def num_split(num):
    digits = (list(str(num)))
    number_of_digits = len(digits) - 1 
    output = []
    for i in digits:
        x = i*10**number_of_digits
        number_of_digits -= 1
        output.append(x)
    return output

num_split(39)