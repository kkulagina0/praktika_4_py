import random


print("Правила игры: \n перед вами лежит случайное число камней из диапазона от 1 до 30\n вы должны забрать от 1 до 3 камней так, чтобы по итогу противнику (то есть компьютеру) остался 1 камень. Удачи ")
N = random.randint(4, 31)
while N > 0:
    try:
        print("Текущее количество камней в куче: ", N)
        polzav_beret = int(input("Введите количествок камней которое хотите взять из кучи: "))
        while polzav_beret > 3 or polzav_beret < 1:
            print("Вы взяли недопустимое количество камней")
            polzav_beret = int(input("Еще раз введите количествок камней которое хотите взять из кучи: "))
            continue
        while N - polzav_beret < 1:
            print("Количество не может быть отрицательным")
            polzav_beret = int(input("Еще раз введите количествок камней которое хотите взять из кучи: "))
            continue
        N -= polzav_beret
        print("Текущее количество камней в куче: ", N)
        if N == 1:
            print("Вы победили!")
            break
        comp_beret = random.randint(1,4)
        while N - comp_beret < 1:
            comp_beret = random.randint(1,4)
            continue
        print("Компьютер взял", comp_beret, "камня")
        N -= comp_beret
        if N == 1:
            print("Текущее количество камней в куче: ", N)
            print("Компьютер победил(")
            break
    except ValueError:
        print("вы ввели недопустимые значение")
