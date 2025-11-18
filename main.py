class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.__grades = []   # maxfiy ro‘yxat

    def add_grade(self, grade):
        self.__grades.append(grade)

    def remove_grade(self, grade):
        if grade in self.__grades:
            self.__grades.remove(grade)

    def get_grades(self):
        return self.__grades.copy()  # tashqi o‘zgartirishdan himoya
