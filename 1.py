print('Введите количество элементов в массиве')
n=int(input()) #n - количество элементов в массиве
arr = []
print('Заполните массив')
for i in range(n):
    x=int(input())
    arr.append(x)
print(arr)
print('Введите значение дельты')
delta = int(input())
chek = [min(arr) - delta, min(arr) + delta]
ans = arr.count(chek[0]) + arr.count(chek[1])
print('Вывод:', ans)