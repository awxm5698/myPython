# all the imports
import sqlite3
import os
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash

# configuration
DATABASE = os.path.join(os.path.abspath("tmp"), "myColl.db")
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    g.db.close()


@app.route('/')
def show_user():
    cur = g.db.execute('select id, login_name, password from user order by id desc')
    # cur = g.db.execute('select id, login_name, password from user order by id desc')

    for c in cur.fetchall():
        print("{}:{}".format(c['Id'], c['Name']))

    user = [dict(id=row[0], name=row[1], password=row[2]) for row in cur.fetchall()]
    status_cur = g.db.execute('select status_name from worker_status')
    status = [dict(name=row[0]) for row in status_cur.fetchall()]
    return render_template("show_user.html", user=user, status=status)


@app.route('/add', methods=['POST'])
def add_user():
    if not session.get('logged_in'):
        abort(401)
    if request.form['name'] != "" or request.form['password'] != "":
        g.db.execute('insert into user (login_name, password) values (?, ?)',
                     [request.form['name'], request.form['password']])
        g.db.commit()
        flash('New entry was successfully posted')
    else:
        flash("The login name or password can't be null")
    return redirect(url_for('show_user'))


@app.route('/delete', methods=['POST'])
def delete_user():
    if not session.get('logged_in'):
        abort(401)
    if request.form['name'] != "":
        g.db.execute('delete from user where login_name = ?', [request.form['name']])
        g.db.commit()
        flash("Delete user successfully")
    else:
        flash("The user id can't be null")
    return redirect(url_for('show_user'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_user'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_user'))


if __name__ == '__main__':
    app.run()
