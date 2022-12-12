from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/infomedia")
def infomedia():
    return render_template("infomedia.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/xrdp")
def xrdp():
    return render_template("xrdp.html")

@app.route("/nomachine")
def nomachine():
    return render_template("nomachine.html")

@app.route("/otherguides")
def otherguides():
    return render_template("otherguides.html")

if __name__ == "__main__":
    app.run()