from flask import Flask, render_template

app = Flask(__name__)

@app.route("/choose-location/")
def choose_location():
    return render_template("index2.html")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
