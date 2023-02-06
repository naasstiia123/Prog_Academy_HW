import logging
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime) s %(name)-12s %(levelname)-8s %(message)s')

filehandler = logging.FileHandler(f'{__name__}.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

class Man:
    def __init__(self, name, surmane, data_birth):
        self.name = name
        self.surname = surmane
        self.data_birth = data_birth

    def __str__(self):
        return f'{self.surname} {self.name[0]}. {self.data_birth}'

class Student(Man):

    def __init__(self, name, surmane, data_birth, ph_num):
        super().__init__(name, surmane, data_birth)
        self.ph_num =ph_num

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'

class Group:

    def __init__(self, title, max_st=10):
        self.title = title
        self.__students = []
        self.max_st = max_st
        self.index = 0

    def __next__(self):
        if self.index < len(self.__students):
            self.index += 1
            return self.__students[self.index-1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def add_st(self, student: Student):
        if not isinstance(student, Student):
            logger.info(f'{student} wrong type of data')
            raise TypeError(f'{student} must be instance of Stodent')
        if len(self.__students) >= self.max_st:
            logger.info(f'{student} Limit')
            raise Limit_students(f'{student} Limit with number of student')
        if student in self.__students:
            logger.info(f'{student} already in group')
            raise ValueError(f'Student {student} already in group')
        logger.info(f'{student}')
        self.__students.append(student)

    def del_st(self, student: Student):
        self.__students.remove(student)


    def find_st(self, surname1: str):
        for i in self.__students:
            if surname1 == i.surname:
                return self.__students
        return -1

    def __str__(self):
        return f'{self.title}\n' + ', '.join(map(str, self.__students))

class Limit_students(Exception):
    def __init__(self, massage):
        super().__init__(massage)
        self.massage = massage
    def error_massage(self):
        return self.massage

if __name__ == '__main__':
    student_1 = Student('Ivan', 'Ivanov', '01.10.2000', '000000000000')
    student_2 = Student('Anastasiia', 'Dzoma', '02.10.2000', '000000000001')
    student_3 = Student('Vladislav', 'Petrov', '03.10.2000', '000000000002')
    student_4 = Student('Roman', 'Samoluk', '04.10.2000', '000000000003')
    student_5 = Student('Andrii', 'Maydanskiy', '05.10.2000', '000000000004')
    student_6 = Student('Sergey', 'Artyuhov', '06.10.2000', '000000000005')
    student_7 = Student('Anna', 'Koltsova', '07.10.2000', '000000000006')
    student_8 = Student('Victoria', 'Grib', '08.10.2000', '000000000007')
    student_9 = Student('Olha', 'Samoylenko', '09.10.2000', '000000000008')
    student_10 = Student('Andrii', 'Kharchenko', '10.10.2000', '000000000009')
    student_11 = Student('Sergey', 'Hmil', '11.10.2000', '000000000010')
    student_12 = Student('Sergey', 'Homenko', '12.10.2000', '000000000011')
    group_1 = Group('Python', 5)

    try:
        group_1.add_st(student_1)
        group_1.add_st(student_2)
        group_1.add_st(student_3)
        group_1.add_st(student_4)
        group_1.add_st(student_5)
        group_1.add_st(student_6)
        group_1.add_st(student_7)
    except Exception as ex:
        pass

    print(group_1)

    for student in group_1:
        print(student)
