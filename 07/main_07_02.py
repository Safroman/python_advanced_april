"""2) Создать базу данных студентов. У студента есть факультет, группа, оценки, номер студенческого билета.
Написать программу, с двумя ролями: Администратор, Пользователь.
Администратор может добавлять, изменять существующих студентов.
Пользователь может получать список отличников, список всех студентов, искать студентов
по номеру студенческого, получать полную информацию о конкретном студенте (включая оценки, факультет)"""
from roles import User, Admin


DB = "07.db"

active_user = Admin(DB)
# active_user = User(DB)

action = ''

if active_user.role == 'admin':
    while True:
        action = input('1. добавить студента; 2. изменить студена; 3. закончить:')

        if action == '1':
            surname = input('фамилия нового студента: ')
            name = input('имя нового студента: ')
            middle_name = input('отчество нового студента: ')
            stud_id = input('студенческий номер нового студента: ')
            faculty_id = input('номер факультета нового студента: ')
            group_name = input('группа нового студента: ')

            active_user.add_student(surname, name, middle_name, stud_id, faculty_id, group_name)

        elif action == '2':

            updates = {}
            stud_id = input('номер студента: ')

            POS_FIELDS = {'1': 'surname', '2': 'name', '3': 'middle_name', '4': 'faculty_id', '5': 'group_name'}

            ans = ''
            while ans != '2':
                print(f'доступные поля {POS_FIELDS}')
                ans = input('что изменить?:')
                field = POS_FIELDS[ans]
                new_value = input('новое значение: ')
                updates[field] = new_value
                ans = input('1 - изменить еще? / 2 - подтвердить?')

            active_user.modify_student(stud_id, updates)

        else:
            break

elif active_user.role == 'user':
    while True:
        action = input('1. список отличников; 2. список всех студентов;'
                       '3. поиск студента; 4. закончить:')

        if action == '1':
            best_students = active_user.get_best_students()
            for el in best_students:
                print(f'{el[1]} {el[2]} {el[3]} (Номер студенческого - {el[0]})')

        elif action == '2':
            students = active_user.get_all_students()
            for el in students:
                print(f'{el[1]} {el[2]} {el[3]} (Номер студенческого - {el[0]})')

        elif action == '3':
            stud_id = input('номер: ')
            stud_info = []
            marks = ()
            try:
                stud_info, marks = active_user.find_student(stud_id)
                print(f'{stud_info[0]} {stud_info[1]} {stud_info[2]}\n'
                      f'Номер студенческого - {stud_info[3]}, факультет {stud_info[4]}, группа {stud_info[5]}')
                for el in marks:
                    print(f'    Предмет - {el[0]}, оценка - {el[1]}')
            except IndexError:
                print(f'В базе нет данных о студенте с номером {stud_id}')
        else:
            break
