from flask import Flask, render_template, request
import json

app = Flask("my_first_app")

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route('/hello')
def hello():
    return 'Hi'

@app.route("/home")
def home_page():
  return render_template("index.html")

@app.route("/about")
def about_page():
  return render_template("about.html")


# app.route("/contact")(lambda: render_template("contact.html")) 
@app.route("/contact")
def contact_page():
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

with open("./static/python_course_members.txt") as input_file:
    python_course_members = [member.strip() for member in input_file]

not_student = ["Pauline", "Lakshika", "Darren", "Nina", "Simon"]

@app.route("/shefcodefirst-members")
def cfg_members():
	return render_template("index.html", members=python_course_members)

@app.route("/shefcodefirst-members/students")
def cfg_studnets():
	students = []
	for name in python_course_members:
		if name not in not_student:
			students.append(name)
	return render_template("index.html", members=students)

# @app.route("/weather/<location>")
# def weather(location):
#   file = json.load("./static/weather_data.json")
#   print(file)
#   return render_template("index.html", members=file)

app.run(debug=True)


