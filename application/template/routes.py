from application import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly_express

@app.route("/")
def index():
    return render_template("layout.html", title = "Home")