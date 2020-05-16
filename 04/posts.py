import datetime


class Post:

    news_feed = []

    def __init__(self, user, title, text):
        self._author = user
        self._title = title
        self._text = text
        self._time_stamp = datetime.date.today()

        Post.news_feed.append(self)
        self._author.new_post(self)

    def __str__(self):
        return f'{self._author} posted: \n{self._text}\ndate:{self._time_stamp}'

    @property
    def title(self):
        return self._title

    @property
    def time_stamp(self):
        return self._time_stamp
