list1 = [1,2,3]
factorial = 1
for i in range(1,len(list1)+1):
    factorial *= i 
num_of_rows = int(factorial / len(list1))
output = []
for i in range(factorial):
    output.append([])

list2 = list1
index1 = 0
u = 0
w = len(list1) - 1
for b in range(len(list1)-1) :
    p = 0
    for i in range(int(len(output)/num_of_rows)):
        y = set(list1).difference(output[index1])
        y1 = list(y)
        [ output[k].append(y1[0]) for k in range(index1,index1+num_of_rows)]
        index1 += num_of_rows
        p += 1
        y = list1

    p = 0
    index1 = 0
    num_of_rows = int(num_of_rows / w)
    w -= 1

output.sort()
output



