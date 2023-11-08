import math


def special_nod(a, b):
    res = 0
    a = abs(a)
    b = abs(b)
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            res = i
            break
    return res


try:
    pervoe = int(input("введите первое число: "))
    vtoroe = int(input("введите второе число: "))
except ValueError:
    print("Неккоректные данные")
else:
    print("НОД созданной функции: ", special_nod(pervoe, vtoroe), "НОД существующей функции: ",
          math.gcd(pervoe, vtoroe))
    print("разница между числами: ", pervoe - vtoroe)