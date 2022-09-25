""" Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """

n = int(input())
arr = list()
for i in range(n):
    arr.append(int(input()))
    
len_arr1 = 0
if len(arr) % 2 == 0:
    len_arr1 = len(arr) // 2
else:
    len_arr1 = len(arr) // 2 + 1

for i in range(len_arr1):
    print(arr[i] * arr[len(arr) - 1 - i])