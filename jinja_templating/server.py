from flask import Flask,render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

# routes
@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    return render_template("index.html",num=random_number,current_year=current_year)

@app.route("/guess/<name>")
def guess(name):
    key = "67619886a6817904944e5b7a"
    URL = f"https://api.genderapi.io/api/?name={name}&key={key}"
    response = requests.get(URL)
    print("Status Code:", response.status_code)  # Print HTTP status code
    if response.ok:  # Check if status code is 200
        data = response.json()
        print("API Response:", data)  # Print the JSON response
    else:
        print("Failed to fetch data from API:", response.text)
    gender_data = data.get("gender", "Not Available") if response.ok else "API Error"
    country = data["country"]
    names_available = data["total_names"]
    return render_template("guess.html", given_name=name.title(), predicted_gender=gender_data,country=country,names_available=names_available)

# URL = f"https://api.genderapi.io/api/?name=maharshi"
# response = requests.get(URL)
# data = response.json()
# print(data)
# gender = data["gender"]
# print(gender)


if __name__ == "__main__":
    app.run(debug=True)