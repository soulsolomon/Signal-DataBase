# Signal-DB (Ongoing)

## Introduction
Quick, reliable data logging is a key requirement for tests from component characterization to prolonged endurance testing to the evaluation of large dataset. This project sets out a way to simulate real-world signals collection, filter and store them in a simple database. This project also provides a platform to interact with stored signal data through Web front-end page. The system invloves the following steps:

* Signal collection
* Filtering 
* Storing in local DB
* Visualization through a local Web-server

<br />

<p align="center">
<img widith=600  src="./image.png">
<p>

  <br />
  
  ## Examples
  
 

<img widith=1000  src="./image2.gif">






  ## Setting Up
    
  ### Front-END
  
  1. Change home directory to \web-server\black-dashboard-flask 
  2. Install dependencies:  pip3 install -r requirements.txt
    
    Set the FLASK_APP environment variable
    # (Unix/Mac) export FLASK_APP=run.py
    # (Windows) set FLASK_APP=run.py
    # (Powershell) $env:FLASK_APP = ".\run.py"
  
    Set up the DEBUG environment
    # (Unix/Mac) export FLASK_ENV=development
    # (Windows) set FLASK_ENV=development
    # (Powershell) $env:FLASK_ENV = "development"
    
  3. run run.py
  4. Create username and password 
  
  
   ### Back-END
    
   1. change home directory to \sensor
   2. Run main.py
  
  ## TASKS YET TO BE ACCOMPLISHED

    Backend
    [Create and simulate Signals - Done!] 
    [Create single database class for different DBMS - Done!] 
    [Create MariaDB database class - Done!] 
    [Create SQLite database class - Done!] 

    Frontend
    [Setup FLASK - Done!] 
    [Create a live stream of sensor data recored - Done!] 
 
  
  ## License 
  GNU General Public License V3.0
    
  
  
  ## Authors
  
  Solomon Gugsa (private work)
    
  Free Design Template used from Black Dashboard Flask - Provided by Creative Tim and AppSeed
  
  ## Version
  
  Initial
  
