from flask import Flask, render_template, request, jsonify
from bot.chat_engine import get_gpt_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = get_gpt_response(user_message)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
