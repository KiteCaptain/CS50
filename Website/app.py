from cs50 import SQL
from flask import Flask, redirect, render_template, request, url_for
import csv 

app = Flask(__name__) 
app.debug = True
db = SQL("sqlite:///clubs.db")

REGISTRANTS = {}

SPORTS = [
    "Football",
    "Basketball",
    "Volleyball",
    "Mathletics"    
]


@app.route("/")
def index():
    return render_template("search.html", name=request.args.get("name", "there!")) 

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form.get("sport") not in SPORTS:
            return render_template("failure.html", sport=request.form.get("sport"))
        name = request.form.get("name")
        sport = request.form.get("sport")
        REGISTRANTS[name] = sport
        with open("registrants.csv", "a", newline="") as csvfile:
            # csvfile.seek(0)
            writer = csv.writer(csvfile)
            if REGISTRANTS:
                for name, sport in REGISTRANTS.items():
                    writer.writerow([name, sport])
        return redirect("/registrants")
    if request.method == 'GET':
        return render_template("register.html", sports=SPORTS)

@app.route("/registrants")
def registrants():
    with open("registrants.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            registrants = {row[0]: row[1] for row in reader}
    return render_template("registrants.html", registrants=registrants)
            
    
    
if __name__ == "__main__":
    app.run(debug=True)