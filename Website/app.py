import os
from cs50 import SQL
from flask import Flask, redirect, render_template, request, url_for
from flask_mail import Mail, Message
import csv 
from dotenv import load_dotenv

app = Flask(__name__) 
app.debug = True
db = SQL("sqlite:///clubs.db")

load_dotenv()

sender = os.getenv("MAIL_DEFAULT_SENDER")
password = os.getenv("MAIL_PASSWORD")
username = os.getenv("MAIL_USERNAME")
print(f"sender: {sender}, password: {password}, username: {username}")


app.config["MAIL_DEFAULT_SENDER"] = sender
app.config["MAIL_PASSWORD"] = password
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = username

# app.config["MAIL_DEFAULT_SENDER"] = "ekaindi5801@gmail.com"
# app.config["MAIL_PASSWORD"] = "khlt okro ctjr qfbm"
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = "ekaindi5801@gmail.com"

mail = Mail(app)

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
        email = request.form.get("email")
        sport = request.form.get("sport")
        REGISTRANTS[email] = sport
        with open("registrants.csv", "a", newline="") as csvfile:
            # csvfile.seek(0)
            writer = csv.writer(csvfile)
            if REGISTRANTS:
                for email, sport in REGISTRANTS.items():
                    writer.writerow([email, sport])
        
        # db.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)",email, sport)        
        
        message = Message(f"Dear {email},Your registration to the {sport} club was successful", recipients=[email])
        message.body = "Congratulations! you have managed to send an email via google smtp server. This is a milestone in your developers journey. Mark this day on your calendar!."
        mail.send(message)
        
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