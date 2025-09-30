from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

choices = ["stone", "paper", "scissors"]

def check_winner(user, comp):
    if user == comp:
        return "Draw"
    if (user == "stone" and comp == "scissors") or \
       (user == "paper" and comp == "stone") or \
       (user == "scissors" and comp == "paper"):
        return "You Win!"
    return "Computer Wins!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.json
    user_choice = data.get("choice")
    comp_choice = random.choice(choices)
    result = check_winner(user_choice, comp_choice)
    return jsonify({
        "user": user_choice,
        "computer": comp_choice,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
