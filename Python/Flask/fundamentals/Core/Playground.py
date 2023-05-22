from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')                           
def welcome():
    return render_template('index.html')  

@app.route('/play/<x>')                           
def welcome(x):
    print(x)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)