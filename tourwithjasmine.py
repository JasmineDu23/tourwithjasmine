from flask import Flask, render_template, request
app = Flask("tourwithjasmine")

@app.route("/")
def homepage():
    return render_template("tourwithjasmine.html")

@app.route("/1")
def japan():
    return render_template("Japan.html")
@app.route("/2")
def london():
    return render_template("London.html")
@app.route("/3")
def paris():
    return render_template("France.html")
@app.route("/4")
def belgium():
    return render_template("Belgium.html")
@app.route("/5")
def iceland():
    return render_template("Iceland.html")
@app.route("/6")
def germany():
    return render_template("Germany.html")

@app.route("/result", methods=["POST"])
def result():
    form_data = request.form
    print (form_data)
    if form_data["Answer"] == form_data["correct"]:
        return render_template("yes.html")
    else:
        return render_template("no.html")

if __name__ == '__main__':
    app.run()
# app.run(debug=True)
