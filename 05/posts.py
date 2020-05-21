import datetime
import shelve


news_feed = 'NewsFeedDB'


def save_post(user, title, text):
    time_stamp = datetime.date.today()
    post = (title, text, time_stamp)
    with shelve.open(news_feed) as db:
        try:
            user_feed = db[user]
            user_feed.append(post)
            db[user] = user_feed
        except KeyError:
            db[user] = [post, ]


def get_posts(user):
    with shelve.open(news_feed) as db:
        try:
            return db[user]
        except KeyError:
            return 'No posts yet'


if __name__ == '__main__':
    with shelve.open(news_feed) as db:
        db.clear()
