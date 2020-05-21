"""4) Дополнение к предыдущей работе с соц. Сетью. Все хранение
данных пользователей реализовать на основе модуля shelve."""

from login import reg_admin, register, sign_in
from posts import save_post, get_posts
from users import populate, population, User

reg_admin()

while True:

    populate()

    ANS1 = ['1', '2']
    ans = None

    print('\nHi visitor!')

    while ans not in ANS1:
        print(f'possible actions:')
        ans = input('1. Register \n2. Sign in\nplease choose :')

    if ans == '1':
        active_user = register()
    else:
        active_user = sign_in()

    ans = None

    if active_user.role == 'user':
        ANS2 = ['1', '2']

        while ans not in ANS2 and ans != '2':
            print(f'possible actions:')
            ans = input('1. Add post \n2. Sign out\nplease choose :')

            if ans == '1':
                name = active_user.u_name
                title = input('type your post title: ')
                text = input('type your post: ')
                save_post(name, title, text)
                ans = None

            elif ans == '2':
                active_user = None
                break

    elif active_user.role == 'admin':
        ANS2 = ['1', '2']

        while ans not in ANS2 and ans != '2':
            print(f'possible actions:')
            ans = input('1. See user list \n2. Sign out\nplease choose :')

            if ans == '1':
                for el in population.keys():
                    user = population[el]
                    print(f'\n{user.u_name} registration date is {user.reg_date}')

                    if get_posts(el) == 'No posts yet':
                        print(f'{user.u_name} have no posts yet')
                    else:
                        for post in user.posts:
                            print(f'user {user.u_name} posted {post[0]} in {post[2]}')

            elif ans == '2':
                active_user = None
                break

            ans = None
