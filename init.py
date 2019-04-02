from add_news import AddNewsForm
from db import DB
from flask import Flask, redirect, render_template, session
from loginform import LoginForm
from news_model import NewsModel
from users_model import UsersModel
from RegForm import Regform
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db = DB()
NewsModel(db.get_connection()).init_table()
UsersModel(db.get_connection()).init_table()


# http://127.0.0.1:8080/login
@app.route('/login', methods=['GET', 'POST'])
def login():
    global form1
    form1 = LoginForm()
    if form1.validate_on_submit():
        user_name = form1.username.data
        password = form1.password.data
        user_model = UsersModel(db.get_connection())
        exists = user_model.exists(user_name, password)
        if (exists[0]):
            session['username'] = user_name
            session['user_id'] = exists[1]
        return redirect("/index")
    return render_template('login.html', title='Авторизация', form=form1)


@app.route('/logout')
def logout():
    session.pop('username', 0)
    session.pop('user_id', 0)
    return redirect('/login')


@app.route('/')
@app.route('/index')
def index():
    if 'username' not in session:
        return redirect('/login')
    news = NewsModel(db.get_connection()).get_all(session['user_id'])
    return render_template('index.html', username=session['username'], news=news)


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    if 'username' not in session:
        return redirect('/login')
    form = AddNewsForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        nm = NewsModel(db.get_connection())
        nm.insert(title, content, session['user_id'], int(time.time()))
        return redirect("/index")
    return render_template('add_news.html', title='Добавление новости', form=form, username=session['username'])


@app.route('/delete_news/<int:news_id>', methods=['GET'])
def delete_news(news_id):
    if 'username' not in session:
        return redirect('/login')
    nm = NewsModel(db.get_connection())
    nm.delete(news_id)
    return redirect("/index")


@app.route('/registration', methods=['GET', 'POST'])
def reg():
    form = Regform()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        UsersModel(1).insert(user_name, password)
        return redirect("/login")
    return render_template('reg.html', title='Регистрация', form=form)


@app.route('/ksdfg12')
def yalox():
    if form1.flag.data == 1:
        return render_template('wasd.html')
    else:
        return redirect('/login')



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
