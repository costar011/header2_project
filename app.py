from flask import Flask, render_template

app = Flask(__name__)

print("Flask Framework ")


@app.route("/")
def base():
    print("indedx!!!!!")
    return render_template("index.html")


@app.route("/in")
def contact():
    print("index2!!!!!!!!!")
    return render_template("index2.html")


app.run(debug=True)
