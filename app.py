from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/nearest_mbta", methods=["POST"])
def nearest_mbta():
    place_name = request.form.get("place")
    try:
        stop, accessible = find_stop_near(place_name)
        return render_template("mbta_station.html", place=place_name, stop=stop, accessible=accessible)
    except Exception as e:
        return f"<h2>Error: {e}</h2><a href='/'>Try again</a>"
    


if __name__ == "__main__":
    app.run(debug=True)
