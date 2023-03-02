from flask import Flask, render_template, request
from ner import SpacyDocument

app = Flask(__name__)


@app.route("/")
def home():
    """
    home page
    :return: a rendered home.html page which contains a form to enter the string.
    """
    return render_template("home.html")


@app.route("/result", methods=["POST"])
def results():
    """
    result page: take in a request from homepage, processes, and display results.
    :return: a rendered results.html page with NER marks
    """
    text = request.form["text_for_NER"]
    sd = SpacyDocument(text)
    return render_template("result.html", result=sd.get_entities_with_markup())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
