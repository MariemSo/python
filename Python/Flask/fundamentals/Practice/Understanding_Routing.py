from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_World():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say(name):
    if name.isalpha():
        print(name)
        return "Hi, " + name+"!"
    else:
        return("Please enter only alphabetical characters for your name.")

@app.route('/users/<number>/<greeting>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(number, greeting):
    if isinstance(greeting, str):
        print (greeting)
    elif isinstance(number, int):
        print (number)
    return '" ' + greeting+' " ' + number + " times"

@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)
