from flask import Flask, render_template, request

app = Flask("my_first_app")

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route('/hello')
def hello():
    return 'Hi'

@app.route('/<number1>/<number2>') #captures whatever you put in <x> 
def add_number(number1, number2):
	result = int(number1) + int(number2)
	return render_template("index.html", result=result)


app.run(debug=True)


