#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число: '))
stepen = 0
while 2** stepen <= N:
    print(2**stepen)
    stepen+=1
