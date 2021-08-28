def get_lucky_number(size, nth):
    list1 = list(range(1,size+1))
    check_list = list1.copy()
    filter1 = 1
    index = filter1
    filter_inter = list1[filter1] 
    while True:
        list2 = []
        for i in range(1,len(list1)):
            list2.append(list1[index])
            index += filter_inter 
            if index >= len(list1):
                break
        list1 = list(set(list1).difference(list2))
        if check_list[filter1] == list1[filter1]: 
            filter1 += 1
            filter_inter = list1[filter1]
        if list1[filter1] > len(list1) : 
            break
        index = filter_inter -1

    return list1

get_lucky_number(25,6)