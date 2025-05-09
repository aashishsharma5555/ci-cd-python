from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI CD Pipeline with docker and github actions"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
