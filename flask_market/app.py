from flask import Flask,render_template

# flask app
app = Flask(__name__)

# home route 
@app.route("/")
def home():
    return render_template("home.html")

# about route
# dynamic route -> passing variables in the url route
@app.route("/about/<username>")
def about_page(username):
    return f"This is the about route for {username}"

# app run 
if __name__ == "__main__":
    app.run(debug=True)
    
    