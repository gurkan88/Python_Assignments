def permutations(list1):
    factorial = 1
    for i in range(1,len(list1)+1):
        factorial *= i 
    num_of_rows = int(factorial / len(list1))
    output = []
    for i in range(factorial):
        output.append([])

    index1 = 0
    y = 0
    u = 0
    w = len(list1) - 1
    while y < len(list1) - 2 :
        while u < len(list1):
            for k in range(index1,index1+num_of_rows):
                output[k].append(list1[u])
            index1 += num_of_rows
            if u+1 != len(list1) : u += 1
            else : u = 0
        index1 = 0
        y += 1
        num_of_rows = int(num_of_rows / w)
        w -= 1

    
    return output

lst = [1,2,3,4,5]
permutations(lst)