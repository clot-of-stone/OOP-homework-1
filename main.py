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
            lecturer.grades.append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        journal = self.grades.values()
        avg = round(sum(journal) / len(journal), 2)
        studies = ', '.join(self.courses_in_progress)
        completed = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:' \
              f' {avg}\nКурсы в процессе изучения: {studies}\nЗавершенные курсы: {completed}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        avg = round(sum(self.grades) / len(self.grades), 2)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg}'
        return res

    def leads(self, course_name):
        self.courses_attached.append(course_name)


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
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

# Выставление оценок студентами лекторам и проверяющими студентам
reviewer_1.rate_hw(student_1, 'Введение в программирование', 8)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_3.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Введение в программирование', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_3.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_3, 'Введение в программирование', 8)
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_3.rate_hw(student_3, 'Git', 10)
student_1.evaluate(lecturer_1, 'Введение в программирование', 8)
student_1.evaluate(lecturer_2, 'Python', 10)
student_1.evaluate(lecturer_3, 'Git', 8)
student_2.evaluate(lecturer_1, 'Введение в программирование', 9)
student_2.evaluate(lecturer_2, 'Python', 9)
student_2.evaluate(lecturer_3, 'Git', 9)
student_3.evaluate(lecturer_1, 'Введение в программирование', 8)
student_3.evaluate(lecturer_2, 'Python', 10)
student_3.evaluate(lecturer_3, 'Git', 7)

# Проверка работы метода __str__ для каждого класса
print(lecturer_1)
print()
print(student_1)
print()
print(lecturer_2)
print()
print(student_2)
print()
print(lecturer_3)
print()
print(student_3)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()
print(reviewer_3)