from flask import Flask, render_template, request
from ner import SpacyDocument
import db

app = Flask(__name__)

entity_db = db.create_db("entities")
# default markup to give back if no text has yet been entered
current_markup = {"markup": "<p class=no_text>No text has been submitted from the Home page.</p>"}


@app.route("/")
def home():
    """
    home page
    :return: a rendered home.html page which contains a form to enter the string.
    """
    return render_template("home.html")


@app.route("/result", methods=["POST", "GET"])
def results():
    """
    result page: take in a request from homepage, processes, and display results.
    :return: a rendered results.html page with NER marks
    """
    if request.method == "POST":
        text = request.form["text_for_NER"]
        sd = SpacyDocument(text)
        [entity_db.add(t, l) for s, e, l, t in sd.get_entities()]
        current_markup["markup"] = sd.get_entities_with_markup()
        return render_template("result.html", result=current_markup["markup"])
    else:
        return render_template("result.html", result=current_markup["markup"])


@app.route("/list_from_db", methods=["GET"])
def list_from_db():
    """
    result page: take in a request from homepage, processes, and display results.
    :return: a rendered results.html page with NER marks
    """
    print(entity_db.get())
    return render_template("list.html", entities=entity_db.get())


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
