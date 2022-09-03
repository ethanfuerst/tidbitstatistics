from app import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html", show_url=True), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html", show_url=True), 500


@app.route("/")
def index():
    return render_template("index.html", show_url=False)


@app.route("/venmo_splitter")
def venmo_splitter():
    return render_template(
        "dashboards/venmo_splitter.html", title="Venmo Splitter", show_url=True
    )


@app.route("/dashboards/nba")
def nba():
    return render_template("dashboards/nba.html", title="NBA Dashboard", show_url=True)


@app.route("/dashboards/imdb_ratings")
def imdb_ratings():
    return render_template(
        "dashboards/imdb_ratings.html", title="IMDb Dashboard", show_url=True
    )


@app.route("/dashboards/bitcoin")
def bitcoin():
    return render_template(
        "dashboards/bitcoin.html", title="Bitcoin Dashboard", show_url=True
    )


@app.route("/dashboards/mpg")
def mpg():
    return render_template("dashboards/mpg.html", title="MPG Dashboard", show_url=True)
