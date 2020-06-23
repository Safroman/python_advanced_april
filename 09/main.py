"""1) Создать базу данных студентов (ФИО, группа, оценки, куратор студента, факультет).
Написать РЕСТ ко всем сущностям в бд (работа со студентами, оценками, кураторами, факультетами).
Создать отдельные контроллер, который будет выводить отличников по факультету."""
from flask import Flask, request, jsonify
import sqlite3


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
app = Flask(__name__)


@app.route('/students', methods=['GET', 'POST'])
@app.route('/students/<stud_id>', methods=['GET', 'PUT', 'DELETE'])
def students(stud_id=None):
    students_struct = {'0': 'id',
                       '1': 'surname',
                       '2': 'name',
                       '3': 'middle_name',
                       '4': 'stud_id',
                       '5': 'faculty_id',
                       '6': 'teacher_id',
                       '7': 'group_name'}

    if request.method == 'GET' and stud_id:
        with DBConnect(DB) as db:
            cursor = db.cursor()
            query = cursor.execute("SELECT * FROM students WHERE stud_id = ?", (stud_id, )).fetchall()[0]
            res = {}
            for i, field in students_struct.items():
                res[field] = query[int(i)]
        return jsonify(res)

    elif request.method == 'GET':
        with DBConnect(DB) as db:
            cursor = db.cursor()
            query = cursor.execute("SELECT * FROM students").fetchall()
            res = {}
            for _ in range(len(query)):
                line = {}
                for i, field in students_struct.items():
                    line[field] = query[_][int(i)]
                    res[_] = line
        return jsonify(res)

    if request.method == 'POST':
        with DBConnect(DB) as db:
            values = request.json.values()
            cursor = db.cursor()
            cursor.execute("INSERT INTO students "
                           "('surname', 'name', 'middle_name', 'stud_id', 'faculty_id', 'teacher_id', 'group_name')"
                           " VALUES (?, ?, ?, ?, ?, ?, ?)", (*values, ))
            db.commit()

        return request.json

    if request.method == 'PUT':
        with DBConnect(DB) as db:
            req_values = request.json
            cursor = db.cursor()
            query = cursor.execute("SELECT * FROM students WHERE id = ?", (stud_id, )).fetchall()[0]
            fields = [el[0] for el in cursor.description]
            new_values = {}
            for i, field in enumerate(fields):
                new_values[field] = query[i]
            for key, value in req_values.items():
                new_values[key] = value
            values = list(new_values.values())
            values.pop(0)
            cursor.execute("UPDATE students SET surname = ?, name = ?, middle_name = ?, stud_id = ?, faculty_id = ?, "
                           "teacher_id = ?, group_name = ? WHERE id = ?", (*values, stud_id))
            db.commit()
        return request.json

    if request.method == 'DELETE' and stud_id:
        with DBConnect(DB) as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (stud_id, ))
            db.commit()
        return request.json


@app.route('/marks', methods=['GET', 'POST'])
@app.route('/marks/<stud_id>', methods=['GET', 'DELETE'])
@app.route('/marks/<stud_id>/<lesson>', methods=['PUT', 'DELETE'])
def marks(stud_id=None, lesson=None):
    marks_struct = {'0': 'id', '1': 'stud_id', '2': 'lesson', '3': 'mark'}

    if request.method == 'GET' and stud_id:
        with DBConnect(DB) as db:
            cursor = db.cursor()
            query = cursor.execute("SELECT * from marks WHERE stud_id = ?", (stud_id, )).fetchall()
            res = {}
            for _ in range(len(query)):
                line = {}
                for i, field in marks_struct.items():
                    line[field] = query[_][int(i)]
                    res[_] = line
        return jsonify(res)

    elif request.method == 'GET':
        with DBConnect(DB) as db:
            cursor = db.cursor()
            query = cursor.execute("SELECT * from marks").fetchall()
            res = {}
            for _ in range(len(query)):
                line = {}
                for i, field in marks_struct.items():
                    line[field] = query[_][int(i)]
                    res[_] = line
        return jsonify(res)

    if request.method == 'POST':
        with DBConnect(DB) as db:
            values = request.json.values()
            cursor = db.cursor()
            cursor.execute("INSERT INTO marks ('stud_id', 'lesson', 'mark') VALUES (?, ?, ?)", (*values, ))
            db.commit()

        return request.json

    if request.method == 'PUT':
        with DBConnect(DB) as db:
            new_mark = request.json['mark']
            cursor = db.cursor()
            cursor.execute("UPDATE marks SET mark = ? WHERE stud_id = ? AND lesson = ?", (new_mark, stud_id, lesson))
            db.commit()
        return request.json

    if request.method == 'DELETE' and stud_id and lesson:
        with DBConnect(DB) as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM marks WHERE stud_id = ? AND lesson = ?", (stud_id, lesson))
            db.commit()
        return request.json
    elif request.method == 'DELETE' and stud_id:
        with DBConnect(DB) as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM marks WHERE stud_id = ?", (stud_id, ))
            db.commit()
        return request.json


@app.route('/teachers', methods=['GET', 'POST'])
@app.route('/teachers/<teacher_id>', methods=['GET', 'PUT', 'DELETE'])
def teachers(teacher_id=None):
    teach_struct = {'0': 'teacher_id', '1': 'surname', '2': 'name', '3': 'middle_name'}

    if request.method == 'GET' and teacher_id:
        with DBConnect(DB) as db:
            cursor = db.cursor()
            query = cursor.execute("SELECT * from teachers WHERE teacher_id = ?", (teacher_id, )).fetchall()[0]
            res = {}
            for i, field in teach_struct.items():
                res[field] = query[int(i)]
        return jsonify(res)

    elif request.method == 'GET':
        with DBConnect(DB) as db:
            cursor = db.cursor()
            query = cursor.execute("SELECT * from teachers").fetchall()
            res = {}
            for _ in range(len(query)):
                line = {}
                for i, field in teach_struct.items():
                    line[field] = query[_][int(i)]
                    res[_] = line
        return jsonify(res)

    if request.method == 'POST':
        with DBConnect(DB) as db:
            values = request.json.values()
            cursor = db.cursor()
            cursor.execute("INSERT INTO teachers ('surname', 'name', 'middle_name') VALUES (?, ?, ?)", (*values, ))
            db.commit()

        return request.json

    if request.method == 'PUT':
        with DBConnect(DB) as db:
            req_values = request.json
            cursor = db.cursor()
            current_values = cursor.execute("SELECT * FROM teachers WHERE teacher_id = ?", (teacher_id, )).fetchall()[0]
            res = list(current_values)
            for key, value in teach_struct.items():
                if value in req_values.keys():
                    res[int(key)] = req_values[value]
                else:
                    res[int(key)] = current_values[int(key)]
            print(res)
            cursor.execute("UPDATE teachers SET surname = ?, name = ?, middle_name = ? "
                           "WHERE teacher_id = ?", (res[1], res[2], res[3], res[0]))
            db.commit()
        return request.json

    if request.method == 'DELETE':
        with DBConnect(DB) as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM teachers WHERE teacher_id = ?", (teacher_id, ))
            db.commit()
        return request.json


@app.route('/faculties', methods=['GET', 'POST'])
@app.route('/faculties/<fac_id>', methods=['GET', 'PUT', 'DELETE'])
def faculties(fac_id=None):
    fac_struct = {'0': 'fac_id', '1': 'fac_name'}

    if request.method == 'GET' and fac_id:
        with DBConnect(DB) as db:
            cursor = db.cursor()
            query = cursor.execute("SELECT * from faculties WHERE fac_id = ?", (fac_id, )).fetchall()[0]

            res = {}
            for i, field in fac_struct.items():
                res[field] = query[int(i)]
        return jsonify(res)

    elif request.method == 'GET':
        with DBConnect(DB) as db:
            cursor = db.cursor()
            query = cursor.execute("SELECT * from faculties").fetchall()
            res = {}
            for _ in range(len(query)):
                line = {}
                for i, field in fac_struct.items():
                    line[field] = query[_][int(i)]
                    res[_] = line
        return jsonify(res)

    if request.method == 'POST':
        with DBConnect(DB) as db:
            new_fac = request.json['fac_name']
            cursor = db.cursor()
            cursor.execute("INSERT INTO faculties ('fac_name') VALUES (?)", (new_fac, ))
            db.commit()

        return request.json

    if request.method == 'PUT':
        with DBConnect(DB) as db:
            new_value = request.json['fac_name']
            cursor = db.cursor()
            cursor.execute("UPDATE faculties SET 'fac_name' = ? WHERE fac_id = ?", (new_value, fac_id))
            db.commit()
        return request.json

    if request.method == 'DELETE':
        with DBConnect(DB) as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM faculties WHERE fac_id = ?", (fac_id, ))
            db.commit()
        return request.json


@app.route('/best', methods=['GET'])
def best():
    with DBConnect(DB) as db:
        cursor = db.cursor()
        query = \
            cursor.execute("SELECT marks.stud_id, surname, name, middle_name FROM marks "
                           "INNER JOIN students ON marks.stud_id = students.stud_id GROUP by marks.stud_id "
                           "HAVING AVG(mark) = 5").fetchall()
        fields = [el[0] for el in cursor.description]
        best_students = {}
        for num, el in enumerate(query):
            data = {}
            for i, field in enumerate(fields):
                data[field] = el[i]
            best_students[num] = data
    return jsonify(best_students)


if __name__ == '__main__':
    app.run(debug=True)
