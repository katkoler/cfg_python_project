from flask import Flask

app = Flask("my_first_app")

@app.route("/")
def say_hello():
  return "hello world!"

app.run(debug=True)
