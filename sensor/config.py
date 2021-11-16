database = {
    "host" : "localhost",
    "user" : "root",
    "password" : "",
    "port" : "3307",
    "database" : "datalogger"
}

sensors = {
    "Sensor 01" : {
        # hertz. [ 0.1Hz = ten times in a second ] [ 2Hz = once in two seconds ] [ 10Hz = once in ten seconds ]
        "data_rate" : 1.0, 
        
        # trigger_value is the value that triggers the system to save the sensor data
        "trigger_value" : 0.0,
        
        # The number of interval the system will wait for a trigger to happen, and if a trigger did not happen the sensor value will be saved after trigger_data_rate count
        # eg. trigger_data_rate = 5. A data will be saved every 5th data_rate after the last saved data.
        "trigger_data_rate" : 5,
        
        # 
        "amplitude" : 5,
        
        #
        "noise_amp" : 2,
        
        # this is implemented in SensorSimulator
        "signal_type" : "sine_wave", # "speed_recored", "tempreture_recored"
        
        # will be store on databse for information
        "remark" : "Dev 4"
    },
    
    "Sensor 02" : {
        "data_rate" : 1.0,
        "trigger_value" : 5.0,
        "trigger_data_rate" : 5,
        "amplitude" : 5,
        "noise_amp" : 2,
        "signal_type" : "sine_wave",
        "remark" : "Dev 4"
    }
}
