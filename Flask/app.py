from flask import Flask, render_template, request
from application.roman_numeral_converter import *

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main_get():
    return render_template("index.html", not_valid=False)


@app.route("/roman", methods=["POST"])
def roman_post():
    alpha = request.form["number"]
    if not alpha.isdecimal():
        return render_template("index.html", not_valid=True)

    number = int(alpha)
    if not 0 < number < 4000:
        return render_template("index.html", not_valid=True)

    return render_template(
        "result_roman.html",
        number_decimal=number,
        number_roman=to_roman_numeral(number),
    )


@app.route("/arabic", methods=["POST"])
def arabic_post():
    alpha = request.form["number"]
    roman = str(alpha).upper()
    if roman.isdecimal():
        return render_template("index.html", not_valid_roman=True)
    return render_template(
        "result_arabic.html",
        number_string=roman,
        number_arabic=to_arabic_number(roman),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3999, debug=True)
