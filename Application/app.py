from flask import Flask, render_template, request
from bp_calculator import get_input, get_results

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("app.html")


@app.route("/send", methods=["POST"])
def send():
    if request.method == "POST":

        systolic_value = request.form["systolic_value"]
        diastolic_value = request.form["diastolic_value"]

        bprisk = get_input(systolic_value, diastolic_value)

        return render_template("app.html", bprisk=bprisk)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

