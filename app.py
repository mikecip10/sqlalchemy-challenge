# Dependencies
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

# Set up
engine = create_engine("sqlite:///Hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Station = Base.classes.station
Measurements = Base.classes.measurements

session = Session(engine)

# Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )
