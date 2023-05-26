from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'visits' in session:
        session['visits']=session.get('visits')+1
        print('key exists!')
    else:
        session['visits'] = 1
        print("key 'key_name' does NOT exist")
    return render_template('index.html', counter=session['visits'])

@app.route('/destroy_session')
def deleteSession():
    session.clear()
    return redirect ('/')

@app.route('/addvisits')
def addvisits():
    counter = session.get('visits') + 1
    session['visits'] = counter

    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)