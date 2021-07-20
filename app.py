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

# Routes
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
@app.route("/api/v1.0/precipitation")
def precipitation():
    last_dt = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    last_yr = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    rain = session.query(Measurements.date, Measurements.prcp).\
        filter(Measurements.date > last_yr).\
        order_by(Measurements.date).all()

    precip = {date: prcp for date, prcp in past_temp}
    
    return jsonify(precip)

@app.route('/api/v1.0/stations')
def stations():

    stations_all = session.query(Station.station).all()

    return jsonify(stations_all)

@app.route("/api/v1.0/tobs")
def tobs():
    last_dt = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    last_yr = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temp = session.query(Measurements.date, Measurements.tobs).\
        filter(Measurements.date > last_yr).\
        order_by(Measurements.date).all()   

    return jsonify(last_yr)

@app.route('/api/v1.0/<start>') 
def start(start=None):

    tobs = (session.query(Measurement.tobs).filter(Measurement.date.between(start, '2017-08-23')).all())
    
    tobs_df = pd.DataFrame(tobs)

    avg = tobs_df["tobs"].mean()
    max = tobs_df["tobs"].max()
    min = tobs_df["tobs"].min()
    
    return jsonify(avg, max, min)

@app.route('/api/v1.0/<start>/<end>') 
def startend(start=None, end=None):

    tobs = (session.query(Measurement.tobs).filter(Measurement.date.between(start, end)).all())
    
    tobs_df = pd.DataFrame(tobs)

    avg = tobs_df["tobs"].mean()
    max = tobs_df["tobs"].max()
    min = tobs_df["tobs"].min()
    
    return jsonify(avg, max, min)


if __name__ == '__main__':
    app.run(debug=True)