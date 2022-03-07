from flask import Flask, jsonify

# Dictionary of Justice League
justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

#################################################
# Flask Setup
#################################################
# @TODO: Initialize your Flask app here
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# @TODO: Complete the routes for your app here
@app.route("/api/v1.0/justice-league")
def justice_league():
    # Return the Justice League dict:
    return jsonify(justice_league_members)

@app.route("/api/v1.0/justice-league/<real_name>")
def justice_league_search(real_name):
    # Return the Justice League character dict:
    canonic_name_version = real_name.replace(" ", "").lower()
    for char in justice_league_members:
        search_term = char["real_name"].replace(" ", "").lower()
        if search_term == canonic_name_version:
            return jsonify(char)
            
    return {"error": f"{real_name} is not a member of the Justice League"}, 404

@app.route("/")
def welcome():
    return(
        f"Welcome to the <b>Justice League</b> API <br/>"
        f"Available Route: <br/>"
        f"/api/v1.0/justice-league - Returns all the Justice League members - <a href='/api/v1.0/justice-league'>Go!</a>"
    )

if __name__ == "__main__":
    app.run(debug=True)
