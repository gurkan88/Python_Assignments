def permutations(list1):
    factorial = 1
    for i in range(1,len(list1)+1):
        factorial *= i 
    num_of_rows = int(factorial / len(list1))
    output = []
    for i in range(factorial):
        output.append([])

    index1 = 0
    for u in list1:
        for k in range(index1,index1+num_of_rows):
            output[k].append(u)
        index1 += num_of_rows

    j,i = 1,0  
    while i < factorial and j < len(list1):
        if list1[j] != output[i][0] :
            output[i].append(list1[j])
            i += 1
            if j+1 != len(list1) : j += 1
            else: j = 0
        else:
            if j+1 != len(list1) : j += 1
            else: j = 0

    for c in range(len(list1)) :
        y = 2
        j,i = 2,0
        while i < factorial and j < len(list1):
            if list1[j] not in output[i][0:y] and output[i] + [list1[j]] not in output:
                output[i].append(list1[j])
                y += 1
                i += 1
                if j+1 != len(list1) : j += 1
                else: j = 0
            else:
                if j+1 != len(list1) : j += 1
                else: j = 0
        y += 1
        
    return output
lst = [1,2,3]
permutations(lst)