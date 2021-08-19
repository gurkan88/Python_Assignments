def multiply_by_11(n):
    x = "0"
    result = ""
    n1 = "".join(("0",n))
    n2 = n + "0"
    for i,j in zip(n1[::-1],n2[::-1]) :
        if int(i) + int(j) + int(x) < 10 :
            result = "".join((str(int(i) + int(j) + int(x)), result))
            x = "0"
        else :
            sum1 = int(i) + int(j) + int(x)
            result = "".join((str(sum1)[-1], result))
            x = f"{sum1 // 10}"
    if x != 0 or x != "0":
        result = "".join((str(x), result))
    return result  




multiply_by_11("86")