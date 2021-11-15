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
  
  <p align="center">
  <img   src="./Screen1.png">
  <p>
    
  
    
  <p align="center">
  <img   src="./Screen2.png">
  <p>
    
  ## Setting Up
  
  1. Change home directory to \web-server\black-dashboard-flask 
  2. Install dependencies:  pip3 install -r requirements.txt
  3. set FLASK_APP=run.py for Windows or export FLASK_ENV=development for Unix/Mac
  4. run run.py
  5. Create username and password 
  
  ## TASKS YET TO BE ACCOMPLISHED

    Backend
    [Create and simulate Signals - Done!] 
    [Create single database class for different DBMS - Done!] 
    [Create MarinaDB database class - Done!] 
    [Create SQLite database class - Done!] 
    [ ] 
    [ ] 

    Frontend
    [Setup FLASK - Done!] 
    [Create a live stream of sensor data recored - partially Done!] 
    [ ] 
    [ ] 
  
  ## License 
  GNU General Public License V3.0
    
  
  
  ## Authors
  
  Solomon Gugsa (private work)
    
  Free Design Template used from Black Dashboard Flask - Provided by Creative Tim and AppSeed
  
  ## Version
  
  Initial
  
