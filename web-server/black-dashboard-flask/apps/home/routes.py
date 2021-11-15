# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import sensor.sensorData


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')

@blueprint.route('/data-logger')
@login_required
def dataLogger():
    
    sensors = getDistinctSensors()
    
    jsStr = ""
    for sensorName in sensors:
        jsStr += getDataForJS(sensorName[0])
    
    data = list()
    data.append(jsStr)
    data.append("This is data")

    return render_template('home/data-logger.html', data = data, segment='data-logger' )



@blueprint.route('/get-data', methods = ['GET'])
@login_required
def getData():
    last = request.args.get('last')
    if(last is None):
        last = 0
    sensors = getDistinctSensors()
    data = dict()
    
    for sensorName in sensors:
        sensorData = sensor.sensorData.getData(sensorName[0], last)
        data.update({sensorName[0]: sensorData})
            
    return str(data)

def getDataForJS(sensorName):
    sensorData = sensor.sensorData.getData(sensorName, 0)
    sensorID = sensorName.replace(" ","_")
    jsStr = sensorID + "_yaxis = ["

    for signalValue in sensorData:
        jsStr += str(signalValue[1]) + ", "
    
    jsStr += "]; \n"
    
    jsStr += sensorID + "_xaxis = ["   
    for i in range(len(sensorData)):
        jsStr += ","
    jsStr += "]; \n"
    
    return jsStr

def getDistinctSensors():
        return sensor.sensorData.getDistinctSensors()



@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            pass

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None