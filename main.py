import ast

students_list = []
lecturers_list = []


def calc_avg_grade(grades):
    journal = grades.values()
    avg = round(sum(journal) / len(journal), 2)
    return avg


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def fin_course(self, course_name):
        self.finished_courses.append(course_name)

    def studies(self, course_name):
        self.courses_in_progress.append(course_name)

    def evaluate(self, lecturer, course_name, grade):
        if isinstance(lecturer, Lecturer) and (course_name in self.finished_courses or course_name in
                                               self.courses_in_progress) and course_name in lecturer.courses_attached:
            if course_name in lecturer.grades:
                lecturer.grades[f'{self.name} {self.surname}'] += grade
            else:
                lecturer.grades[f'{self.name} {self.surname}'] = grade
        else:
            return 'Ошибка'

    def __le__(self, other):
        if not isinstance(other, Student) or not isinstance(self, Student):
            return f'Нельзя сравнивать представителей разных групп!'
        elif isinstance(other, Student) and isinstance(self, Student):
            if calc_avg_grade(self.grades) < calc_avg_grade(other.grades):
                return f'{self.name} {self.surname} имеет среднюю оценку ниже, чем {other.name} {other.surname}'
            elif calc_avg_grade(self.grades) > calc_avg_grade(other.grades):
                return f'{self.name} {self.surname} имеет среднюю оценку выше, чем {other.name} {other.surname}'
            else:
                return f'{self.name} {self.surname} и {other.name} {other.surname} имеют одинаковую среднюю оценку.'
        else:
            print(f'Проверьте введённые данные!')

    def __str__(self):
        studies = ', '.join(self.courses_in_progress)
        completed = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:' \
              f' {calc_avg_grade(self.grades)}\nКурсы в процессе изучения: {studies}\nЗавершенные курсы: {completed}\n'
        return res

    def __repr__(self):
        return f'name={self.name}, surname={self.surname}, grades={self.grades})'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {calc_avg_grade(self.grades)}\n'
        return res

    def leads(self, course_name):
        self.courses_attached.append(course_name)

    def __le__(self, other):
        if not isinstance(other, Lecturer) or not isinstance(self, Lecturer):
            return f'Нельзя сравнивать представителей разных групп!'
        elif isinstance(other, Lecturer) and isinstance(self, Lecturer):
            if calc_avg_grade(self.grades) < calc_avg_grade(other.grades):
                return f'{self.name} {self.surname} имеет среднюю оценку ниже, чем {other.name} {other.surname}'
            elif calc_avg_grade(self.grades) > calc_avg_grade(other.grades):
                return f'{self.name} {self.surname} имеет среднюю оценку выше, чем {other.name} {other.surname}'
            else:
                return f'{self.name} {self.surname} и {other.name} {other.surname} имеют одинаковую среднюю оценку.'
        else:
            print(f'Проверьте введённые данные!')


class Reviewer(Mentor):
    def rate_hw(self, student, course_name, grade):
        if isinstance(student, Student) and course_name in self.courses_attached and \
                (course_name in student.courses_in_progress or course_name in student.finished_courses):
            if course_name in student.grades:
                student.grades[course_name] += grade
            else:
                student.grades[course_name] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


# Наполнение БД студентов и преподавателей
student_1 = Student('Виктор', 'Малинин', 'M')
student_1.studies('Git')
student_1.fin_course('Введение в программирование')
student_1.fin_course('Python')

student_2 = Student('Елена', 'Перепёлкина', 'F')
student_2.studies('Python')
student_2.studies('Введение в программирование')
student_2.fin_course('Git')

student_3 = Student('Марина', 'Веточкина', 'F')
student_3.studies('Git')
student_3.studies('Python')
student_3.fin_course('Введение в программирование')

lecturer_1 = Lecturer('Артём', 'Аистов')
lecturer_1.leads('Введение в программирование')

lecturer_2 = Lecturer('Гвидон', 'Змеев')
lecturer_2.leads('Python')

lecturer_3 = Lecturer('Яков', 'Умнов')
lecturer_3.leads('Git')

reviewer_1 = Reviewer('Максим', 'Кнутов')
reviewer_1.courses_attached += ['Введение в программирование']

reviewer_2 = Reviewer('Софья', 'Пряникова')
reviewer_2.courses_attached += ['Python']

reviewer_3 = Reviewer('Игорь', 'Круглов')
reviewer_3.courses_attached += ['Git']

# Выставление оценок студентами лекторам; выставление оценок проверяющими студентам
reviewer_1.rate_hw(student_1, 'Введение в программирование', 8)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_3.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Введение в программирование', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_3.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_3, 'Введение в программирование', 8)
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_3.rate_hw(student_3, 'Git', 10)
student_1.evaluate(lecturer_1, 'Введение в программирование', 9)
student_1.evaluate(lecturer_2, 'Python', 10)
student_1.evaluate(lecturer_3, 'Git', 8)
student_2.evaluate(lecturer_1, 'Введение в программирование', 9)
student_2.evaluate(lecturer_2, 'Python', 9)
student_2.evaluate(lecturer_3, 'Git', 9)
student_3.evaluate(lecturer_1, 'Введение в программирование', 8)
student_3.evaluate(lecturer_2, 'Python', 10)
student_3.evaluate(lecturer_3, 'Git', 8)

# Проверка работы метода __str__ для каждого класса
print(student_1)
print(student_2)
print(student_3)
print(lecturer_1)
print(lecturer_2)
print(lecturer_3)
print(reviewer_1)
print(reviewer_2)
print(reviewer_3)

# Проверка возможности сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и
# студентов по средней оценке за домашние задания
print(student_1 <= student_2)
print(student_3 >= student_1)
print(lecturer_1 <= student_1)
print(lecturer_1 <= lecturer_2)
print(lecturer_3 >= lecturer_1)

# Наполнение оценками списков для передачи в функции для подсчёта средней оценки за ДЗ по всем студентам в рамках
# конкретного курса и средней оценки за лекции всех лекторов в рамках курса
students_list.append(f'{student_1.grades}')
students_list.append(f'{student_2.grades}')
students_list.append(f'{student_3.grades}')
lecturers_list.append(f'{lecturer_1.grades}')
lecturers_list.append(f'{lecturer_2.grades}')
lecturers_list.append(f'{lecturer_3.grades}')

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса)


def count_avg_hw_grade(id_list, course_name):
    a = 0
    for i in range(0, len(id_list)):
        journal = ast.literal_eval(id_list[i])
        for subject in journal.keys():
            if subject == course_name:
                a += journal.get(subject)
    result = round(a / len(id_list), 2)
    if result > 0:
        print(f'Средняя оценка студентов за домашние задания на курсе {course_name}: {result}')
    else:
        print('Ошибка ввода названия курса')

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса)


def count_avg_lessons_grade(id_list, course_name):
    marks = []
    if course_name == 'Введение в программирование':
        journal = ast.literal_eval(id_list[0])
        for mark in journal.values():
            marks.append(mark)
    elif course_name == 'Python':
        journal = ast.literal_eval(id_list[1])
        for mark in journal.values():
            marks.append(mark)
    elif course_name == 'Git':
        journal = ast.literal_eval(id_list[2])
        for mark in journal.values():
            marks.append(mark)
    else:
        print('Ошибка ввода названия курса')
        return
    result = round(sum(marks) / len(marks), 2)
    line = f'Средняя оценка лектора на курсе {course_name}: {result}'
    print(line)


print()
count_avg_hw_grade(students_list, 'Введение в программирование')
count_avg_hw_grade(students_list, 'Python')
count_avg_hw_grade(students_list, 'Git')
count_avg_hw_grade(students_list, 'абырвалг')
print()
count_avg_lessons_grade(lecturers_list, 'Введение в программирование')
count_avg_lessons_grade(lecturers_list, 'Python')
count_avg_lessons_grade(lecturers_list, 'Git')
count_avg_lessons_grade(lecturers_list, 'абырвалг')
