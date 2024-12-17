from flask import Flask

# creating flask app
app = Flask(__name__)

# print(app) #<Flask 'server'>

# creating our routes
@app.route("/")
def say_hello():
    return "My first flask app."

@app.route("/home")
def home_page():
    return "Home page"

# adding multiple variables 
@app.route("/<username>/<int:age>")
def profile(username,age):
    return f"my name is {username} and my age is {age}"

if __name__ == "__main__":
    # making debug to activate
    # auto reload
    app.run(debug=True)