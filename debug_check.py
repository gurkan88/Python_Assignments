def num_grid(lst):
    import copy
    default = copy.deepcopy(lst)
    coordinate = lst[::-1]
    dict1 = {}
    
    for y in range(len(lst)):
        for x in range(len(lst[0])):
            coordinate[y][x] = [y,x]
            dict1.update({"{}".format(coordinate[y][x]):"{}".format(default[y][x])})
    dict2 = copy.deepcopy(dict1)
    lst.insert(0,[])
    lst.append([])
    lst[0] = [[5,i] for i in range(-1,len(default[0])+1)]
    lst[6] = [[-1,i] for i in range(-1,len(default[0])+1)]
    for i,j in enumerate(range(4,-1,-1),1):
        lst[i].append([j,5])
    for i,j in enumerate(range(4,-1,-1),1):
        lst[i].insert(0,[j,-1])
    for y in lst:
        for x in y:
            if str(x) not in dict2.keys():
                dict2.update({"{}".format(x):None})
    
    import ast
    for i,j in dict1.items():
        if j == "-":
            count = 0
            change = copy.deepcopy(i)
            i = ast.literal_eval(i)
            y, x = i[0], i[1]
            i = [y, x+1]
            for a in [y-1,y,y+1]:
                i = [a, x+1]
                if dict2["{}".format(i)] == "#":
                    count += 1
            i = [y, x]
            for b in [y-1, y+1]:
                i = [b, x]
                if dict2["{}".format(i)] == "#":
                    count += 1
            i = [y, x-1]
            for c in [y-1, y, y+1]:
                i = [c, x-1]
                if dict2["{}".format(i)] == "#":
                    count += 1
            dict2[change] = count

    for i in lst:
        for j in range(len(lst[0])):
            if "{}".format(i[j]) in dict2.keys():
                i[j] = dict2["{}".format(i[j])]
    
    for i in range(len(lst)):
        lst[i] = list(filter(lambda x : x != None, lst[i]))
    
    lst = list(filter(None,lst))
    return lst

    

num_grid([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]
])