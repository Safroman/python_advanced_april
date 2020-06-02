from connector_07_01 import DBConnect


class Admin:

    def __init__(self, db):
        self._db_name = db
        self._role = 'admin'

    @property
    def role(self):
        return self._role

    def add_student(self, *args):

        with DBConnect(self._db_name) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO students ('surname', 'name', 'middle_name', 'stud_id', 'faculty_id', "
                           "'group_name') VALUES (?, ?, ?, ?, ?, ?)", [*args])
            db.commit()
        print('student was added successfully')

    def modify_student(self, stud_id, updates):
        students_structure = {
            'id': 0,
            'surname': 1,
            'name': 2,
            'middle_name': 3,
            'stud_id': 4,
            'faculty_id': 5,
            'group_name': 6
        }

        with DBConnect(self._db_name) as db:
            cursor = db.cursor()
            values = list(cursor.execute("SELECT * FROM students WHERE stud_id = ?", (stud_id, )).fetchall()[0])

            for key, value in updates.items():
                values[students_structure[key]] = value
            values.append(stud_id)

            cursor.execute("UPDATE students SET 'id' = ?, 'surname' = ?, 'name' = ?, 'middle_name' = ?, 'stud_id' = ?, "
                           "'faculty_id' = ?, 'group_name' = ? WHERE stud_id = ?", values)
            db.commit()

        print('Данные успешно обновлены')


class User:

    def __init__(self, db):
        self._db_name = db
        self._role = 'user'

    @property
    def role(self):
        return self._role

    def get_best_students(self):
        with DBConnect(self._db_name) as db:
            cursor = db.cursor()
            best_students = \
                cursor.execute("SELECT DISTINCT marks.stud_id, surname, name, middle_name FROM marks "
                               "INNER JOIN students ON marks.stud_id = students.stud_id WHERE mark = 5")
            return best_students.fetchall()

    def get_all_students(self):
        with DBConnect(self._db_name) as db:
            cursor = db.cursor()
            students = cursor.execute("SELECT stud_id, surname, name, middle_name FROM students")
            return students.fetchall()

    def find_student(self, stud_id):
        with DBConnect(self._db_name) as db:
            cursor = db.cursor()
            stud_info = cursor.execute("SELECT surname, name, middle_name, stud_id, faculties.fac_name, group_name "
                                       "FROM students INNER JOIN faculties ON students.faculty_id = faculties.fac_id "
                                       "WHERE students.stud_id = ?", (stud_id,)).fetchall()
            marks = cursor.execute("SELECT lesson, mark FROM marks WHERE stud_id = ?", (stud_id,)).fetchall()
            return stud_info[0], marks
