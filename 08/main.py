from flask import Flask, render_template, request
import sqlite3


DB = 'goods.db'
app = Flask(__name__)


class DBConnect:

    def __init__(self, db_name):
        self._db_name = db_name
        self._conn = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._db_name)
        return self._conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()


@app.route('/')
def start():
    res = None
    with DBConnect(DB) as db:
        cursor = db.cursor()
        res = cursor.execute("SELECT * FROM categories").fetchall()
    return render_template('index.html', categories=res)


@app.route('/<category>')
def show_category(category):
    goods = None
    with DBConnect(DB) as db:
        cursor = db.cursor()
        res = cursor.execute("SELECT name FROM goods INNER JOIN categories ON goods.category_id = "
                             "categories.category_id WHERE category_name = ? AND amount > ?", (category, '0')).fetchall()
        goods = {}
        for num, el in enumerate(res):
            goods[num+1] = el[0]

        return render_template('category.html', goods=goods, category=category)


@app.route('/<category>/<item>')
def show_item(category, item):
    with DBConnect(DB) as db:
        cursor = db.cursor()
        res = cursor.execute("SELECT * FROM goods WHERE name = ?", (item, )).fetchall()
        return render_template('item.html', item=res[0])


@app.route('/admin', methods=["GET", "POST"])
def admin():
    if len(request.form) == 1:
        new_cat = request.form['category']
        with DBConnect(DB) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO categories(category_name) VALUES (:new_cat)", {'new_cat': new_cat})
            db.commit()

    elif len(request.form) == 5:
        res = []
        for el in request.form.values():
            res.append(el)

        with DBConnect(DB) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO goods(name, category_id, availability, price, amount) "
                           "VALUES (?, ?, ?, ?, ?)", res)
            db.commit()

    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
