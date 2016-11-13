import os

from flask import Flask, request, render_template
app = Flask(__name__)

items = [
        {
            'id':1,
        'from': 'zen@no.com',
        'to': 'eugine@why.do',
        'subject': 'why do we have to do thissss',
        'time': '5:34 pm',
        'insides': 'dear eugine, my friend pooh says to store the ',
            'labels': ['fun', 'not fun'],
        }, {
            'id':2,
        'from': 'zen@no.com',
        'to': 'eugine@why.do',
        'subject': 'why do we have to do thissss',
        'time': '5:34 pm',
        'insides': 'dear eugine, my friend pooh says to store the honey',
            'labels': ['fun', 'not fun', 'honey'],
        }, {

        'id': 3,
        'from': 'zen@no.com',
        'to': 'eugine@why.do',
        'subject': 'why do we have to do thissss',
        'time': '5:34 pm',
        'insides': 'dear eugine, my friend pooh says to store',
            'labels': ['fun', 'not fun'],
        }, {

        'id': 4,
        'from': 'zen@no.com',
        'to': 'eugine@why.do',
        'subject': 'why do we have to do thissss',
        'time': '5:34 pm',
        'insides': 'dear eugine, my friend pooh says to store the honey',
            'labels': ['fun', 'not fun', 'honey'],
        }, {

        'id': 5,
        'from': 'zen@no.com',
        'to': 'eugine@why.do',
        'subject': 'why do we have to do thissss',
        'time': '5:34 pm',
        'insides': 'dear eugine, my friend pooh says to store the honey',
            'labels': ['fun', 'not fun', 'honey'],
        }
    ]

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def log_the_user_in(username):
    return render_template('email_list.html', emails=items, user=username)

def valid_login(username, password):
    if 'dog' in username and 'cat' in password:
        return True

    return False

@app.route("/emails")
def emails():
    return render_template('email_list.html', emails = items*3)


@app.route('/emails/<int:email_id>')
def show_email(email_id):
    # assume we get email from the email id

    return render_template('emails.html', item=items[email_id - 1])


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
