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

if __name__ == "__main__":
    app.run()