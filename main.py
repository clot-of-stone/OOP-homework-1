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
        if isinstance(lecturer, Lecturer) and course_name in self.finished_courses and \
                course_name in lecturer.courses_attached:
            if course_name in lecturer.grades:
                lecturer.grades[course_name] += [grade]
            else:
                lecturer.grades[course_name] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(self, Mentor)
        self.lectures_grades = []
        self.grades = {}

    def leads(self, course_name):
        self.courses_attached.append(course_name)

    def add_lectures(self, course_name):
        self.lectures_grades.append(course_name)


class Reviewer(Mentor):
    def rate_hw(self, student, course_name, grade):
        if isinstance(student, Student) and course_name in self.courses_attached and \
                course_name in student.courses_in_progress:
            if course_name in student.grades:
                student.grades[course_name] += [grade]
            else:
                student.grades[course_name] = [grade]
        else:
            return 'Ошибка'
    pass


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

lecturer_1 = Lecturer('Яков', 'Умнов')
# print(lecturer_1.__dict__)

reviewer_1 = Reviewer('Максим', 'Кнутов')
reviewer_1.courses_attached += ['Python']
reviewer_1.rate_hw(best_student, 'Python', 10)

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

student_1 = Student('Виктор', 'Малинин', 'M')
student_1.studies('Git')
student_1.studies('Django')
student_1.fin_course('Python')


student_2 = Student('Елена', 'Перепёлкина', 'F')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Django']
student_2.finished_courses += ['Git']

student_3 = Student('Марина', 'Веточкина', 'F')
student_3.courses_in_progress += ['Django']
student_3.finished_courses += ['Python']
student_3.finished_courses += ['Git']

student_4 = Student('Игорь', 'Лысиков', 'M')
student_4.courses_in_progress += ['Git']
student_4.finished_courses += ['Python']
student_4.finished_courses += ['Django']

student_5 = Student('Наталья', 'Пуговкина', 'F')
student_5.finished_courses += ['Git']
student_5.finished_courses += ['Python']
student_5.finished_courses += ['Django']

student_6 = Student('Виталий', 'Наливкин', 'M')
student_6.courses_in_progress += ['Git']
student_6.courses_in_progress += ['Python']
student_6.courses_in_progress += ['Django']

print(best_student.grades)

# help(Student)

print(student_1.__dict__)
