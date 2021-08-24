list1 = [1,2,3,4,5,6,7,8,9]
factorial = 1
for i in range(1,len(list1)+1):
    factorial *= i 
num_of_rows = int(factorial / len(list1))
output = []
for i in range(factorial):
    output.append([])

index1 = 0
u = 0
w = len(list1) - 1
for b in range(len(list1)-1) :
    p = 0
    for i in range(int(len(output)/num_of_rows)):
        y = set(list1).difference(output[index1])
        y1 = list(y)
        [ output[k].append(y1[p]) for k in range(index1,index1+num_of_rows)]
        index1 += num_of_rows
        if p+1 != len(y1) : p += 1
        else :              p = 0
        y = list1

    p = 0
    index1 = 0
    num_of_rows = int(num_of_rows / w)
    w -= 1

for q in range(len(output)):
    diff = set(list1).difference(output[q])
    output[q].append(*diff)

output