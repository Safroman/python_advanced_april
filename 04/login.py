from users import User


def register():
    log = input('What is your name? :')

    while log in User.population.keys():
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
            u = User(log, pw1)
            return u


def sign_in():

    log = input('Enter your name? :')

    while log not in User.population.keys():
        log = input("this name doesn't exist, choose another name:")

    u = User.population[log]

    pw = input('type your password: ')

    while pw != u.u_pw:
        pw = input('password is incorrect, try again: ')

    print(f'Welcome back {u.u_name}\n')
    return u
