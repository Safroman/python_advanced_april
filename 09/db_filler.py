"""2) Создать модуль, который будет заполнять базу данных
случайными валидными значениями (минимум 100 студентов)."""
import sqlite3
from random import choice


class DBConnect:

    def __init__(self, db_name):
        self._db_name = db_name
        self._conn = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._db_name)
        return self._conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()


DB = "09_auto_filled.db"

SEX = ['M', 'W']

M_SURNAMES = ['Анисимов', 'Шаров', 'Демьянов', 'Сахаров', 'Седов', 'Анисимов', 'Русаков', 'Митрофанов', 'Маркин',
              'Поликарпов']
M_NAMES = ['Алексей', 'Архип', 'Станислав', 'Ефим', 'Вячеслав', 'Cлава', 'Филипп', 'Афанасий', 'Андрей', 'Олег']
M_MIDDLE_NAMES = ['Аскольдович', 'Анварович', 'Данилович', 'Вячеславович', 'Петрович', 'Никитич', 'Демидович',
                  'Вадимович', 'Владленович', 'Пахомович']

W_SURNAMES = ['Лаврентьева', 'Губанова', 'Дмитриева', 'Фокина', 'Чеботарева', 'Дружинина', 'Щеглова', 'Булатова',
              'Покровская', 'Копылова']
W_NAMES = ['Евангелина', 'Эльвира', 'Камилла', 'Алена', 'Ника', 'Евгения', 'Зарина', 'Нина', 'Ярослава', 'Полина']
W_MIDDLE_NAMES = ['Кирилловна', 'Антоновна', 'Станиславовна', 'Петровна', 'Владовна', 'Ильясовна', 'Назаровна',
                  'Гаврииловна', 'Климовна', 'Александровна']

GROUPS = ['A', 'B', 'C']
LESSONS = ['Math', 'English', 'IT']


with DBConnect(DB) as db:
    cursor = db.cursor()
    fac_list = [el[0] for el in cursor.execute("SELECT fac_id FROM faculties").fetchall()]
    teach_list = [el[0] for el in cursor.execute("SELECT teacher_id FROM teachers").fetchall()]


def gen_students(num):
    stud_id = '0001'
    stud_list = []

    for i in range(num):
        sex = choice(SEX)
        if sex == 'M':
            row = (choice(M_SURNAMES), choice(M_NAMES), choice(M_MIDDLE_NAMES))
        else:
            row = (choice(W_SURNAMES), choice(W_NAMES), choice(W_MIDDLE_NAMES))

        row += (stud_id, )
        stud_id = str(int(stud_id)+1)
        stud_id = str('0' * (4 - len(stud_id))) + stud_id
        row += (choice(fac_list), )
        row += (choice(teach_list), )
        row += (choice(GROUPS), )

        stud_list.append(row)

    with DBConnect(DB) as db:
        cursor = db.cursor()
        cursor.executemany("INSERT INTO students "
                           "('surname', 'name', 'middle_name', 'stud_id', 'faculty_id', 'teacher_id', 'group_name') "
                           "VALUES (?, ?, ?, ?, ?, ?, ?)", stud_list)
        db.commit()

    return None


def gen_marks(num):
    with DBConnect(DB) as db:
        cursor = db.cursor()
        stud_list = [el[0] for el in cursor.execute("SELECT stud_id FROM students").fetchall()]

    marks = []
    for stud in stud_list:
        for _ in range(num):
            row = ()
            row += (stud, )
            row += (choice(LESSONS), )
            row += (choice([2, 3, 4, 5]), )
            marks.append(row)

    with DBConnect(DB) as db:
        cursor = db.cursor()
        cursor.executemany("INSERT INTO marks('stud_id', 'lesson', 'mark') VALUES (?, ?, ?)", marks)
        db.commit()

    return None


gen_students(10)
gen_marks(3)
