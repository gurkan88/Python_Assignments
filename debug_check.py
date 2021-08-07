text = input('Enter a text > ')
liste = ['(', '{', '[', ')', '}', ']']
dictt = {'(':')', '{':'}', '[':']', ')':'(', '}':'{', ']':'['}
leng = len(text)
result = True
for i in text:
    if i in liste:
        sayi_1 = text.count(i)
        x = text.find(i)
        tersi = dictt[i]
        if tersi in text:
            sayi_2 = text.count(tersi)
            y = text[::-1].find(tersi)
            y = leng - y - 1
            if i == '(' or i == '{' or i == '[':
                if sayi_1 !=sayi_2 or x > y or not (y - x) % 2:
                    result = False
                    break
            else:
                if y > x:
                    if i not in text[y + 1:]:
                        result = False
                        break
        else:
            result = False
    else:
        result = False
print(result)