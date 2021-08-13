def lcm(nums):
    lcm1 = dict()
    factors = []
    result = 1
    for i in nums :
        key = i
        lcm1.update({i : []})
        for j in range(2,i) :
            if i % j == 0 :
                i /= j
                lcm1[key].append(j)
                while i % j == 0 :
                    i /= j
                    lcm1[key].append(j)
    for k in lcm1.values() :
        factors += k 
    factors = set(factors)

    for k in factors :
        number_of_factors = list(map(lambda x : x.count(k), lcm1.values()))
        result *= k ** max(number_of_factors)

    return result
            

v = [5,5,5]
lcm(v)