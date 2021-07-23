def Prime_number_check(num):
    if num.replace(" ","").isdigit():
        num = int(num)
        division = int(num/2 + 0.5)  #to have less calculation, the greatest divider is half of the number
        if num % 2 == 0:        # check if even number
            if num == 2:
                print(f"{num} is a prime number")
            else:
                print(f"{num} is not a prime number")
        elif num == 0:
            print(f"{num} is not a prime number")
        elif num == 1:
            print(f"{num} is not a prime number")
        elif num == 3:
            print(f"{num} is a prime number")
        elif num == 5:
            print(f"{num} is a prime number")
        else:
            for i in range(3,division):    
                if num % i == 0 :
                    return print(f"{num} is not a prime number")
                else:
                    return print(f"{num} is a prime number") 
    else:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

input1 = input("Enter a number: ")
Prime_number_check(input1)
