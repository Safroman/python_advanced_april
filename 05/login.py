import shelve
import datetime
from users import User, population


user_list = 'UsersDB'


def reg_admin():
    reg_time = datetime.date.today()
    with shelve.open(user_list) as db:
        db['admin'] = ('admin', 'adm1', reg_time, 'admin')


def register():
    log = input('What is your name? :')

    with shelve.open(user_list) as db:
        while log in db.keys():
            log = input('this name is already taken, choose another name:')

    while True:
        pw1 = input('type your password: ')

        while pw1.isdigit() or pw1.isalpha() or not pw1.isalnum():
            print('password have to consists of letters and numbers: ')
            pw1 = input('type your password: ')

        pw2 = input('please repeat your password: ')

        if pw1 != pw2:
            print("passwords doesn't match")
        else:
            reg_date = datetime.date.today()
            with shelve.open(user_list) as db:
                db[log] = (log, pw2, reg_date, 'user')

            return User(log, pw1, reg_date)


def sign_in():

    log = input('Enter your name? :')

    with shelve.open(user_list) as db:
        while log not in db.keys():
            log = input("this name doesn't exist, choose another name:")
        pw_ = db[log][1]

    pw = input('type your password: ')

    while pw != pw_:
        pw = input('password is incorrect, try again: ')

    print(f'Welcome back {log}\n')
    return population[log]
