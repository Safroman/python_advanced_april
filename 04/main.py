from login import register, sign_in
from users import User
from posts import Post


admin = User('admin', 'admin1', 'admin')

while True:

    ANS1 = {'1': register, '2': sign_in}
    ans = None

    print('\nHi visitor!')

    while ans not in ANS1.keys():
        print(f'possible actions:')
        ans = input('1. Register \n2. Sign in\nplease choose :')

    active_user = ANS1[ans]()

    ans = None

    if active_user.role == 'user':
        ANS2 = ['1', '2']

        while ans not in ANS2 and ans != '2':
            print(f'possible actions:')
            ans = input('1. Add post \n2. Sign out\nplease choose :')

            if ans == '1':
                title = input('type your post title: ')
                text = input('type your post: ')
                Post(active_user, title, text)
                ans = None

            elif ans == '2':
                active_user = None
                break

    elif active_user.role == 'admin':
        ANS2 = ['1', '2', '3']

        while ans not in ANS2 and ans != '3':
            print(f'possible actions:')
            ans = input('1. See user list \n2. See last 3 posts\n3. Sign out\nplease choose :')

            if ans == '1':
                for el in User.population.keys():
                    user = User.population[el]
                    print(f'\n{user} registration date is {user.reg_date}')
                    for p in User.population[el].posts:
                        print(f'{user} posted {p.title} in {p.time_stamp}')

            elif ans == '2':
                for i, p in enumerate(Post.news_feed):

                    if i < 3:
                        print(Post.news_feed[-i-1])
                    else:
                        break

            elif ans == '3':
                active_user = None
                break

            ans = None
