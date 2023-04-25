from flask import Flask, render_template, request, redirect, session, make_response
from datetime import datetime, timedelta, timezone

app = Flask(__name__, template_folder='templates')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)
app.secret_key = 'EXA844'


@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        running_time = (datetime.now(timezone.utc) -
                        session.get('_creation_time'))
        remaining_time = app.permanent_session_lifetime - running_time
        counter_value = request.args.get('counter', default=0, type=int) + 1
        counter_login = request.cookies.get('counter_login')

        resp = render_template('counter.html', counter=counter_value,
                               username=username, remaining_time=remaining_time, counter_login=counter_login)
    else:
        if 'counter_login' in request.cookies:
            count = request.cookies.get('counter_login')
        else:
            count = "0"
        resp = make_response(
            'Bem-vindo, você fez ' + count + ' logins no site! <br><br> <a href = "/login"> Login </a>')

    return resp


@app.route('/login', methods=['GET'])
def loginHtml():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    if 'counter_login' in request.cookies:
        count = int(request.cookies.get('counter_login'))
    else:
        count = 0

    username = request.form['username']
    session['username'] = username
    session['_creation_time'] = datetime.now(timezone.utc)

    resp = redirect('/')
    resp.set_cookie('counter_login', str(
        count + 1).encode('utf-8'), max_age=60*60*24)

    return resp


if __name__ == '__main__':
    app.run(debug=True)
