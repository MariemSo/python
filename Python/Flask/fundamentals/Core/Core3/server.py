from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

app = Flask(__name__)
app.secret_key = 'Safety101' 


