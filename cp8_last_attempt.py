def bin2(n):
    s = ''
    while n != 0:
        s = str(n % 2) + s
        n //= 2
    return s
def bin8(n):
    s = ''
    while n != 0:
        s = str(n % 8) + s
        n //= 8
    return s
n = int(input('Введите десятичное число:'))
n1 = n
while 1:
    try:
        ss = int(input('Введите основание системы счисления для перевода:'))
        if ss == 2 or ss == 8:
            break
        else:
            print('Ошибка. Введите основание равное 2 или 8')
            continue
    except:
        print('Ошибка')
        continue
if ss == 2:
    print(n1, '->', bin2(n))
else:
    print(n1, '->', bin8(n))
    