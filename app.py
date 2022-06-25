#from flask import Flask
#app = Flask(__name__)
#@app.route('/')
#@app.route('/')
#def hello_world():
 #   return 'Hello world'

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
# Access the sqlite database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

#Reflect the database
Base.prepare(engine, reflect=True)

# Create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from python to our database
session = Session(engine)

# Create a flask application
app = Flask(__name__)

# Define welcome route 
@app.route("/")

#Create a function welcome
def welcome():
    return

# Add the precipitation, stations. tobs and temp routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
