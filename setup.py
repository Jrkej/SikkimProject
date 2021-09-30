# The simple and incredible Flask lib to create backend for websites using python.
from flask import Flask, render_template, request, redirect, url_for

# Application declaration.
app = Flask(__name__)

# Defining website links.
@app.route("/")
def main():
    return redirect(url_for("home"))

@app.route("/home",methods=["GET","POST"]) # Homepage
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        page = request.form['redirect']
        return redirect(url_for(page))

@app.route("/introduction",methods=["GET","POST"]) # Introduction Page
def introduction():
    if request.method == "GET":
        return render_template("introduction.html")
    else:
        page = request.form['redirect']
        return redirect(url_for(page))

@app.route("/flora",methods=["GET","POST"]) # Flora Information page
def flora():
    if request.method == "GET":
        return render_template("flora.html")
    else:
        page = request.form['redirect']
        return redirect(url_for(page))

@app.route("/fauna",methods=["GET","POST"]) # Fauna Information Page
def fauna():
    if request.method == "GET":
        return render_template("fauna.html")
    else:
        page = request.form['redirect']
        return redirect(url_for(page))

@app.route("/sources",methods=["GET","POST"]) # Sources page
def sources():
    if request.method == "GET":
        return render_template("sources.html")
    else:
        page = request.form['redirect']
        return redirect(url_for(page))

@app.errorhandler(404) # Error Handler
def not_found(link):
    return redirect(url_for("error"))

@app.route("/error",methods=["GET","POST"])
def error():
    if request.method == "GET":
        return render_template("Invalid.html")
    else:
        page = request.form['redirect']
        return redirect(url_for(page))

if __name__ == "__main__":
    app.run()
