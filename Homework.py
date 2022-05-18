# Класс студент. Можем создать студента, необходимо передать имя, фамилию, пол
# Студенту можно присвоить курс который он проходит или проходил, а также поставить оценку
# Студент может оценивать лектора, для этого студент указывает преподавателя, курс и оценку.
import random


class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    # Метод оценивания лектора студентом
    def rate_lecturer(self,student, lecturer, course, grade):
        if grade <= 10 and grade >= 1:
            if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            # else:
            #     print("Err")
        else:
            print("Оценка больше 10 или меньше 1")

    # Средняя оценка по всем предметам за домашние задания
    def average(self):
        try:
            summa = []
            for k,v in self.grades.items():
                    summa = summa + v
            return sum(summa)/len(summa)
        except ZeroDivisionError:
            return f"Нет оценок"

    # сравнение студентов по средней оценке по всем курсам
    def __lt__(self, other):
        if self.average() == other.average():
            return "Средняя оценка одинакова"
        elif self.average() > other.average():
            return f"{self.name} {self.surname} средняя оценка больше {self.average()} чем у {other.name} {other.surname} у него всего {other.average()}"

        else:
            return f"{self.name} {self.surname} средняя оценка меньше {self.average()} чем у {other.name} {other.surname} у него  {other.average()}"


    # Изменяем вывод print
    def __str__(self):
        return f"""
        СТУДЕНТ
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.average()}
        Курсы в процессе изучения:{str(self.courses_in_progress).strip('[]')}
        Завершенные курсы:{str(self.finished_courses).strip('[]')}"""

# Ментор главный класс от которого создаются Лектор и Проверяющий. Запрашивает Имя, Фамилию, Курс
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Лектор, читает лекции по своему курсу. Его могут оценивать студенты. Ставить оценки не может.
class Lecturer(Mentor):
    lecture_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecture_list.append(self)

    def __str__(self):
        return f"""
        ЛЕКТОР
        Имя: {self.name}
        Фамилия: {self.surname}
        Ведет курс: {self.courses_attached}
        Средняя оценка за лекции: {self.average()} """

    def average(self):
        try:
            summa = []
            for k,v in self.grades.items():
                    summa = summa + v
            return round(sum(summa)/len(summa),2)
        except ZeroDivisionError:
            return f"Нет оценок"

# сравнение лекторов по средней оценке по всем курсам
    def __lt__(self, other):
        if self.average() == other.average():
            return "Средняя оценка по всем лекциям одинакова"
        elif self.average() > other.average():
            return f"{self.name} {self.surname} средняя оценка больше {self.average()} чем у {other.name} {other.surname} у него всего {other.average()}"

        else:
            return f"{self.name} {self.surname} средняя оценка меньше {self.average()} чем у {other.name} {other.surname} у него  {other.average()}"



# Проверяющий, проверяет работу студента и выставляет ему оценку
class Reviewer(Mentor):
    reviewer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        Reviewer.reviewer_list.append(self)
    # Функция для проставления оценки ученикам
    def rate_hw(self, student, course, grade):
        if grade <= 10 and grade >= 1:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            # else:
            #      print('Ошибка')
        else:
            print(f"Оценка больше {course} 10 или меньше 1. Ввели {grade}")

    def __str__(self):
        return f"""
        ПРОВЕРЯЮЩИЙ
        Имя: {self.name}
        Фамилия: {self.surname}
        Проверяет курс: {self.courses_attached}
"""



def courses_average_student(student_list,course):
    res = ""
    for student in student_list:

        for k,v in student.grades.items():
            if course == k:
                sum_average = sum(v)/len(v)
                res += f"Студент: {student.name} {student.surname}\nКурс: {k}\n"f"Cредняя оценка за домашние задания: {round(sum_average, 1)}\n"
            else:
                "NO COURSE"
    return res

def courses_average_lecturer(lecturer_list,course):
    for lecturer in lecturer_list:
        for k,v in lecturer.grades.items():
            if course == k:
                sum_average = sum(v)/len(v)
                return f"Лектор: {lecturer.name} {lecturer.surname}\nКурс: {k}\n" f"Cредняя оценка за курс: {round(sum_average, 1)}\n"



def count_student():
    count_stud = {}
    for student in Student.student_list:
        if student.courses_in_progress not in count_stud:
            count_stud[student.courses_in_progress] = 1
        else:
            count_stud[student.courses_in_progress] += 1
    return count_stud



l = [("Misha", "Ivanov", "m"),("Sasha", "Rutn", "m"),("Dina", "Svire", "g"),("Misha", "Kash", "m"),("Risha", "Bee", "m"),("Sre", "Ntr", "m")]
language = ["Python", "C", "Git", "Math"]
i = 0

# Генерируем студентов и  лекторов и проверяющих
while len(Student.student_list) < 10:
    for name,surname,gender in l:
            student = Student(name,surname,gender)
            student.courses_in_progress = random.choice(language)
            if len(Lecturer.lecture_list) < len(language):
                lecturer = Lecturer("Lecturer"+name,surname)
                lecturer.courses_attached = language[i]

            if len(Reviewer.reviewer_list) < len(language):
                reviewer = Reviewer("Reviewer"+name,surname)
                reviewer.courses_attached = language[i]
            i+=1

# Ставим оценки лекторам и студентам
for i in Student.student_list:
    for j in Lecturer.lecture_list:
        i.rate_lecturer(i, j, i.courses_in_progress, random.randint(1,10))
        for x in Reviewer.reviewer_list:

            x.rate_hw(i, x.courses_attached, random.randint(1,10))


print(f''' 
Всего учеников {len(Student.student_list)}
Всего преподавателей  {len(Lecturer.lecture_list)}
Всего проверяюших  {len(Reviewer.reviewer_list)}
На курсе {count_student()} студентов
Сравним студентов {Student.student_list[0] > Student.student_list[1]}
Сравним лекторов {Lecturer.lecture_list[0] > Lecturer.lecture_list[1]}

Средняя оценка за домашние задания по Python у студентов 
{courses_average_student(Student.student_list,"Python")}

Средняя оценка за курс Python у лектора
{courses_average_lecturer(Lecturer.lecture_list,"Python")}

Выведем на экран студента, лектора и проверяющего
{Student.student_list[0]}
{Lecturer.lecture_list[0]}
{Reviewer.reviewer_list[0]}

''')




# # По умолчанию создаем 2 учеников, 2 лекторов, 2 проверяющих
# first_student,second_student = Student('Первый', 'Студент', 'м'), Student('Второй', 'Студент', 'ж')
#
# # Первого зачислим на Python, второго на Java
# first_student.courses_in_progress += ['Python']
# second_student.courses_in_progress += ['Java']
#
# # Лектор Python and Java
# python_lecturer = Lecturer('Лектор', 'по Python')
# python_lecturer.courses_attached += ['Python']
# java_lecturer = Lecturer('Лектор', 'по Java')
# java_lecturer.courses_attached += ['Java']
#
# # Проверяющий Python and Java
# first_reviewer = Reviewer('Проверяющий', 'по Python')
# first_reviewer.courses_attached += ['Python']
# second_reviewer = Reviewer('Проверяющий', 'по Java')
# second_reviewer.courses_attached += ['Java']
#
# # Поставим оценки студентам
# first_reviewer.rate_hw(first_student, 'Python', 1)
# first_reviewer.rate_hw(first_student, 'Python', 1)
# second_reviewer.rate_hw(second_student, 'Java', 10)
# second_reviewer.rate_hw(second_student, 'Java', 10)
#
# # Поставим оценки лекторам
# first_student.rate_lecturer(first_student,python_lecturer,"Python",4)
# first_student.rate_lecturer(first_student,python_lecturer,"Python",9)
#
# second_student.rate_lecturer(second_student,java_lecturer,"Java",1)
# second_student.rate_lecturer(second_student,java_lecturer,"Java",9)
#
# # for i in Student.student_list:
# #   print(i)
# # for j in Lecturer.lecture_list:
# #      print(j)
#
# print(f"""
# {first_student < second_student}
# {python_lecturer < java_lecturer}
#
# {courses_average_student(Student.student_list, "Java")}
# {courses_average_lecturer(Lecturer.lecture_list, "Python")}
#
# """)
# # {first_student}
# # {second_student}
# # {second_student.grades}
# # {second_student.average("Java")
# # {python_lecturer}
# # {java_lecturer}
# #
# # {first_reviewer}
# # {second_reviewer}


