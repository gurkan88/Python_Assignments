def truncatable(n):
    numR, numL = str(n), str(n)
    listR, listL = [numR], [numL]
    for i in range(len(str(n))):
        numR = numR.rstrip(numR[-1])
        if numR != "":  
            listR.append(numR)
    for i in range(len(str(n))):
        numL = numL.lstrip(numL[0])
        if numL != "": 
            listL.append(numL)

    listL_check = []
    for i in listL:
        if i[0] != 0:
            i = int(i)
            prime_check = False
            if (i != 1) and (i != 0):
                for j in range(2,i):
                    if (i % j == 0): prime_check = True
                if prime_check == False : listL_check.append(str(i))
    listR_check = []
    for i in listR:
        if i[0] != 0:
            i = int(i)
            prime_check = False
            if (i != 1) and (i != 0):
                for j in range(2,i):
                    if (i % j == 0): prime_check = True
                if prime_check == False : listR_check.append(str(i))

    if (listL_check == listL) and (listR_check == listR):
        return "both"
    elif (listL_check == listL): return "left"
    elif (listR_check == listR): return "right"
    else : return False


truncatable(7331)
