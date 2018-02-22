from flask import Flask, render_template, request

app = Flask("my_first_app")

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route('/hello')
def hello():
    return 'Hi'

@app.route("/home")
def home():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")  


@app.route('/<number1>/<number2>') #captures whatever you put in <x> and renders it into html
def add_number(number1=0, number2=0):
	result = int(number1) + int(number2)
	return render_template("index.html", result=result)


@app.errorhandler(404)
def error(error):
    return render_template('error.html'), 404

@app.route("/<name>")
def say_hello_to(name):
  return render_template("hello.html", user=name)

@app.route("/feedback", methods=["POST"])
def get_feedback():
  # request.values is a dictionary holding any
  # POST request data that's not already part of the URL
  data = request.values
  form_name = data["name"]

  return render_template("feedback.html", form_data=data)




app.run(debug=True)


