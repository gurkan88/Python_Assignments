def polybius(text):
    text = text.upper().replace("J","I")
    import string
    upper = string.ascii_uppercase.replace("IJ","I")
    dict1 = {}
    for j in range(0,25):
        row = j // 5 + 1
        column = j % 5 + 1
        dict1[f"{row}{column}"] = upper[j]
    if text[0].isalpha():
        dict1 = {str(k): str(v) for v, k in dict1.items()}
        for i in text:
            if i != " ": text = text.replace(i, dict1[i])
        return text
    else:
        decode = [i for i in text.split(" ") if i]
        for i in range(len(decode)) :
            n = 2
            decode[i] = [decode[i][j:j+n] for j in range(0,len(decode[i]),2)]
            for k in range(int(len(decode[i])/2)):
                decode[i][k] = dict1[decode[i][k]]
           

    return decode

polybius("2324 4423154215")