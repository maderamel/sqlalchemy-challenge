# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available routes"""
    return(
        f"Welcome! What would you like to know about the weather?<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
        f"Please input dates in YYYY-MM-DD format"
    )
        
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    #query to get 12mo precipitation data
    year_prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > '2016-08-22').order_by(Measurement.date).all()
    session.close()

    prcp_data = []

    for date, prcp in year_prcp_data:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_data.append(prcp_dict)


    return jsonify(prcp_data)


@app.route("/api/v1.0/stations")
def stations():
    
    station_list = session.query(Station.station, Station.id).all()
    session.close()

    stations_data = []

    for station, id in station_list:
        station_dict = {}
        station_dict["station"] = station
        station_dict["id"] = id
        stations_data.append(station_dict)    
    
    return jsonify(stations_data)   
        
@app.route("/api/v1.0/tobs")
def tobs():
  
    yr_station_temp = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date > '2016-08-22').all()
    session.close()

    yr_list = []

    for date, tobs in yr_station_temp:
        yr_dict = {}
        yr_dict["date"] = date
        yr_dict["tobs"] = tobs
        yr_list.append(yr_dict)

    return jsonify(yr_list)



@app.route("/api/v1.0/<start>")
def starts(start): 
    st_que = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start)
    session.close()
    st_list = []

    for min, max, avg in st_que:
        st_dict = {}
        st_dict["min"] = min
        st_dict["max"] = max
        st_dict["avg"] = avg
        st_list.append(st_dict)

    return jsonify(st_list)

@app.route("/api/v1.0/<start>/<end>")
def ends(start,end):  
    stend_que = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end)
    session.close()
    stend_list = []

    for min, max, avg in stend_que:
        stend_dict = {}
        stend_dict["min"] = min
        stend_dict["max"] = max
        stend_dict["avg"] = avg
        stend_list.append(stend_dict)

    return jsonify(stend_list) 
    
        
        
if __name__ == '__main__':
    app.run()        
        
        
        
        
        

