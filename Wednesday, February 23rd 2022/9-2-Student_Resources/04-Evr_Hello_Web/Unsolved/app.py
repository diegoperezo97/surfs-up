# 1. Import Flask
from socketserver import ThreadingUnixStreamServer
from unicodedata import name
from flask import Flask

# 2. Create an app
app = Flask(__name__)

# 3. Define index route
@app.route("/")
def index():
    return "Welcome!"

# 4. Define the about route
@app.route("/about")
def about():
    name = "Diego"
    location = "CDMX"
    return f"My name is {name} and you can find me in {location}!"

# 5. Define the contact route
@app.route("/contact")
def contact():
    email = "diego.perez.ortega43@gmail.com"
    return f"Contact me at: {email}"

# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=ThreadingUnixStreamServer)