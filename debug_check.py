def prime_factors(num):
    factors = []
    prime_numbers = []
    num12 = num
    i = 2
    for i in range(2,num):
        if num % i == 0:
            factors.append(i)
            num /= i
            while num % i == 0:
                factors.append(i)
                num /= i
                if num % i != 0: break
    for j in range(2,int(num12)):
        count = 0
        for k in range(2,j+1):
            if j % k == 0:
                count += 1
        if not count >= 2:
            prime_numbers.append(j)
    for m in factors:
        if m not in prime_numbers:
            factors.remove(m)
    return num12

prime_factors(128000)