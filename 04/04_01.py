import abc
from datetime import datetime


class AbstractPerson(abc.ABC):

    current_date = datetime.date(datetime.now())

    @abc.abstractmethod
    def show(self):
        print(f"Here is person's {self._name} information :")

    @abc.abstractmethod
    def current_age(self):
        pass


class Applicant(AbstractPerson):

    def __init__(self, s_name, b_date, faculty):
        self._name = s_name
        self._b_date = datetime.date(datetime.strptime(b_date, "%d.%m.%Y"))
        self._age = self.current_age()
        self._faculty = faculty

    def __str__(self):
        return f"Applicant {self._name}"

    def current_age(self):
        return (datetime.date(datetime.now()) - self._b_date).days // 365

    def age(self):
        return self._age

    def show(self):
        super().show()
        print(f' Name: {self._name},'
              f'\n Birth date: {self._b_date: %d.%m.%Y},'
              f'\n Faculty: {self._faculty},'
              f'\n age: {self._age}.')


class Student(AbstractPerson):

    def __init__(self, s_name, b_date, faculty, course):
        self._name = s_name
        self._b_date = datetime.date(datetime.strptime(b_date, "%d.%m.%Y"))
        self._age = self.current_age()
        self._faculty = faculty
        self._course = course

    def __str__(self):
        return f"Student {self._name}"

    def current_age(self):
        return (datetime.date(datetime.now()) - self._b_date).days // 365

    def age(self):
        return self._age

    def show(self):
        super().show()
        print(f' Name: {self._name},'
              f'\n Birth date: {self._b_date: %d.%m.%Y},'
              f'\n Faculty: {self._faculty},'
              f'\n age: {self._age},'
              f'\n course: {self._course}.')


class Teacher(AbstractPerson):

    def __init__(self, s_name, b_date, faculty, pos, exp):
        self._name = s_name
        self._b_date = datetime.date(datetime.strptime(b_date, "%d.%m.%Y"))
        self._age = self.current_age()
        self._faculty = faculty
        self._pos = pos
        self._exp = exp

    def __str__(self):
        return f"Teacher {self._name}"

    def current_age(self):
        return (datetime.date(datetime.now()) - self._b_date).days // 365

    def age(self):
        return self._age

    def show(self):
        super().show()
        print(f' Name: {self._name},'
              f'\n Birth date: {self._b_date: %d.%m.%Y},'
              f'\n Faculty: {self._faculty},'
              f'\n age: {self._age},'
              f'\n position: {self._pos},'
              f'\n experience: {self._exp}.')


A1 = Applicant('apl_1', '10.10.2000', 'some faculty')
A2 = Applicant('apl_2', '10.05.1990', 'some faculty')
S1 = Student('stud_1', '10.05.1999', 'some faculty', 1)
S2 = Student('stud_2', '10.05.1998', 'some faculty', 2)
T1 = Teacher('teach_1', '10.05.1988', 'some faculty', 'position', 5)
T2 = Teacher('teach_2', '10.05.1958', 'some faculty', 'position', 10)

p_list = [A1, A2, S1, S2, T1, T2]

for el in p_list:
    el.show()


class AgeChk(ValueError):
    def __init__(self):
        pass


while True:

    try:
        s_age = int(input('select minimal age'))
        if s_age <= 0:
            raise AgeChk
        e_age = int(input('select maximal age'))
        if e_age <= 0:
            raise AgeChk

    except AgeChk:
        print("age can't be 0 or below")

    except ValueError:
        print('type only numbers !')

    else:
        break

for el in p_list:
    if el.age() >= s_age and el.age() <= e_age:
        print(f'{el} - {el.age()}')

