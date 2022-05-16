# class Person:
#     def __init__(self, id):
#         self.id = id
# some_person = Person(100)
# some_person.__dict__["age"] = 30
# print(dir(some_person))
# print(some_person.age)
# print(some_person.__dict__)
#
# print(some_person.age + len(some_person.__dict__))

# class Income:
#     def __init__(self, id_):
#         self.id_ = id_
#         id_ = 100
# income1 = Income(1)
# print(income1.__dict__)

# print("I'm a student and I'll become a \"strong\" programmer")
# print(r"C:\Users\GoodStudent")

# count = int(input("Сколько чашек кофе?"))
# if count >= 6:
#     print("Оплати 5 одна в подарок")
# else:
#     print("Гони бабки")

# xa, ya = int(input("xa ")), int(input("ya "))
# xb, yb = int(input("xb ")), int(input("yb "))
# AB = ((xb - xa)**2 + (yb - ya)**2)**0.5
# print(AB)

# list = list(range(1,101))
# print(list)
# for i in list:
#     print(f'{i} на {i} равно {i*i}')

# numbers = [1,2,3,4,5]
#
# for i, item in enumerate(numbers):
#     numbers[i] *=2
#     print(f"{i} и {item}")

# person =[("Vlad",25), ("Sasha", 26), ("Olga",23)]
#
# for (name, age) in person:
#     print(f"{name} is {age} years old")

#
# person_dict = {
#     "Vlad": 25,
#     "Sasha": 26,
#     "Olga": 24
# }
#
# print(person_dict)
# print(person_dict.items())
# for k,v in person_dict.items():
#         print(f"{k} is {v}")
#
#
# numbers = [n*n for n in range(0,11)]
# print(numbers)
#
# numbers1 = [n*n for n in range(0,11) if n%2!=0]
# print(numbers1)
#
# rating = [100, 34, 55, 66, 67,89]
# titles = ["A" if x > 90 else "B" for x in rating]
# print(titles)


# star = int(input("Введите количество строк "))
# for i in range(1,star+1):
#     print("*" * i)
#
# num = int(input("Введите число "))
# for i in range(0,num+1):
#     if i%2 == 0:
#         print(f"{i} is Even")
#     else:
#         print(f"{i} is Odd ")
#
# limit = 5 # получили ввод числа от пользователя, например 10
# sum = 0
# for i in range(limit + 1):
#     if i%3 == 0 or i%5 == 0:
#         sum +=i
# print(sum)



# first_lst = [1,2,3,4,5,6]
# second_lst = [10,11,12,13,14,15]
# # ваше решение ниже:
# joined_list = []
#
# for num in first_lst:
#     if num % 2 != 0:
#         joined_list.append(num)
#
# for num2 in second_lst:
#     if num2 % 2 == 0:
#         joined_list.append(num2)
#
# print(joined_list)


# #Игра
# current_hand = [2,3,4,10,"Q",5]
# #current_hand = ["A",3,4,10,"J",4]
# ball = {
#     2:1,
#     3:1,
#     4:1,
#     5:1,
#     6:1,
#     7:0,
#     8:0,
#     9:0,
#     10:-1,
#     "J":-1,
#     "Q":-1,
#     "K":-1,
#     "A":-1
# }
# cards_sum = 0
#
# for k, v in ball.items():
#         if k in current_hand:
#             cards_sum += v
#
# cards = sum(ball[x] for x in current_hand) # второе решение
#
# print(cards)

# table_cards =["A_S", "J_H", "7_D", "8_D", "10_D"]
# hand_cards = ["J_D", "3_D"]
#
# table = [x[x.find("_") + 1:] for x in table_cards]
# hand = [x[x.find("_") + 1:] for x in hand_cards]
#
# card_suit = ["S","H","D","C"]
# flush = ""
# for x in card_suit:
#     s_table = table.count(x)
#     s_hand = hand.count(x)
#     if s_table + s_hand >= 5:
#         flush = "Flush!"
#         break
#     else:
#         flush = "No Flush!"
# print(flush)
import random

#угадай число
# comp_number = random.randint(1,50)
# i = 0
# while i < 6:
#     number = int(input("Enter the number "))
#     if comp_number > number:
#         print("Загаданное число больше")
#         i += 1
#     elif comp_number < number:
#         print("Загаданное число меньше")
#         i += 1
#     elif comp_number == number:
#         print("Ты угадал число")
#         break


# # камень ножницы бумага
# import random
# l = {"r":"Камень", "s":"Ножницы", "p":"Бумага"}
# winner = [("r","s"),("s","p"),("p","r")]
# conti = True
# while conti:
#     user_choise = input("Введите R - Камень, S - Ножницы, P - бумага ").lower()
#     comp_choise, comp_name = random.choice(list(l.items()))
#
#
#     if user_choise not in list(l.keys()):
#         print("Вы ввели неправильную команду")
#         continue
#
#     print(f"Компьютер выбрал {comp_name}")
#     if user_choise == comp_choise:
#         print("Ничья")
#     elif (user_choise,comp_choise) in winner:
#         print(f"Ты победил {l[user_choise]} бьют {comp_name}")
#     else:
#         print(f"Компьютер победил {comp_name} бьют {l[user_choise]} ")
#
#     should_conti = input("Продолжить игру? Y or N ").lower()
#     if should_conti == "y":
#         continue
#     else:
#         conti = False

# palindrome

# number = int(input("Enter a number "))
#
# tmp_number = number
# revers_number = 0
#
# while tmp_number > 0:
#
#     revers_number = (revers_number * 10) + tmp_number%10
#     tmp_number = tmp_number // 10
#
# if number == revers_number:
#     print("Palindrom")
# else:
#     print("No palidrom")

# def square(*args):
#     return [x*x for x in args]
# result = square(1,2,3,4,5)
# print(result)

# p1 = "   Bang!"
# p2 = " Bang!"
#
# def whos_first(p1,p2):
#     if p1.index("B") < p2.index("B"):
#         print("p1 стреляет быстрее p2")
#     else:
#         print("p2 стреляет быстрее p1")
#
# whos_first(p1,p2)


# lst = [(1,2),(3,4),(5,5)]
# def calc_dice_scores(lst):
#     res = 0
#     for one,two in lst:
#         if one == two:
#             res = 0
#             return res
#             break
#         else:
#             res = res + one + two
#     return res
#
# print(calc_dice_scores(lst))



# square = [[1,2,3], [4,5,6],[7,8,9]]
# def any_duplicates(square):
#     lst = []
#     for i in square:
#         for j in i:
#             if j in lst:
#                 return True
#             else:
#              lst.append(j)
#     return False
# print(any_duplicates(square))

# pal = 10
#
# while pal > 0:
#     print("Игрок 1 - берет")
#     first = int(input("Сколько палочек берешь? от 1 до 3 "))
#     print(f"Игрок 1 взял {first} палочек. Осталось {pal-first}")
#     pal = pal - first
#
#     if pal == 0:
#         print("Победил игрок first")
#         break
#
#     print("Игрок 2 - берет")
#     second = int(input("Сколько палочек берешь? от 1 до 3 "))
#     print(f"Игрок 2 взял {second} палочек. Осталось {pal - second}")
#     pal = pal - second
#     if pal == 0:
#         print("Победил игрок second")
#         break


# class Tuti():
#     RACE = 100
#
#     def __init__(self,name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
# unit = Tuti("Vlad")
# unit1 = Tuti("Olga")
#
# print(unit1._Tuti__name)
# print(unit.name)

# while True:
#     sum = int(input("Введите сумму ").replace(" ", ""))
#     inf = float(input("Введите инфляцию "))
#     year = int(input("Введите количество лет "))
#     result = (sum * (1+inf/100)**year)
#     postpone = (result/year)/12
#     print(f"Для накопления состояния {sum} с ежегодной инфляцией {inf} за {year} лет. Потребуется {round(result)}. Для достижения цели необходимо Ежемесячно откладывать {round(postpone)} ")
#
#     cont  = input("Продолжить? ")
#     if cont == "y":
#         continue
#     else:
#         break
#

# fruits = ["Apple", "Banana", "Lemon"]
# fruits_dictionary = {fruit:"In stock" for fruit in fruits}
# print(fruits_dictionary)


class Student:
    def __init__(self, name,surname,gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
first = Student("Tom", "RRR", "man")
first.finished_courses += ["Git"]
first.finished_courses += ["Tit"]
print(first.surname)
print(first.finished_courses)

