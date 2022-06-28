class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def studies(self, course_name):
        self.courses_in_progress.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

first_student = Student('Виктор', 'Малинин', 'M')
first_student.studies('Git')
first_student.studies('Django')
first_student.add_courses('Python')

second_student = Student('Елена', 'Перепёлкина', 'F')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Django']
second_student.finished_courses += ['Git']

third_student = Student('Марина', 'Веточкина', 'F')
third_student.courses_in_progress += ['Django']
third_student.finished_courses += ['Python']
third_student.finished_courses += ['Git']

fourth_student = Student('Игорь', 'Лысиков', 'M')
fourth_student.courses_in_progress += ['Git']
fourth_student.finished_courses += ['Python']
fourth_student.finished_courses += ['Django']

fifth_student = Student('Наталья', 'Пуговкина', 'F')
fifth_student.finished_courses += ['Git']
fifth_student.finished_courses += ['Python']
fifth_student.finished_courses += ['Django']

sixth_student = Student('Виталий', 'Наливкин', 'M')
sixth_student.courses_in_progress += ['Git']
sixth_student.courses_in_progress += ['Python']
sixth_student.courses_in_progress += ['Django']

print(best_student.grades)

# help(Student)

print(first_student.__dict__)