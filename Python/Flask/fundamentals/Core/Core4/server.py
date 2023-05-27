from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

#Render Route - Display
@app.route('/')
def index():
    return render_template('index.html')

#Action route - Process the form
@app.route('/process', methods=["POST"])
def submitForm():
    session["name"] =request.form["name"]
    session["location"]=request.form["location"]
    session["language"]=request.form["language"]
    session["comment"]=request.form["comment"]
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")
 
if __name__=="__main__":
    app.run(debug=True)