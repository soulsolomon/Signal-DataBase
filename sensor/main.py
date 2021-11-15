from os import system, name
import time
from datetime import datetime
import config
from SensorSimulator import SensorSimulator
from database.MyDB import MyDB

#------------------------------------------------------------------------------------------------------------------------
def main():
    
    sensor_list = create_sensor_list()
    cnt = 0
    while(True):
        for sensor in sensor_list:
            date_time = datetime.now()
            
            save, signal = sensor.get_sensor_data()
            
            if(save):
                save_on_db(date_time, sensor.sensor_name, signal, sensor.remark)
                system('cls')
                print_saved_data(date_time, sensor.sensor_name, signal, sensor.remark)
            else:
                # save_on_db(date_time, sensor.sensor_name, signal, "NOT SAVED")
                pass
        
        time.sleep(.1)
        cnt += 1
        #if(cnt > 20):
        #    break
        
    
    #print_data()

#------------------------------------------------------------------------------------------------------------------------

def save_on_db(date_time, sensor_name, sensor_value, remark):
    
    insert_query = "INSERT INTO log (date_time, sensor_name, sensor_value, remark) VALUES (?, ?, ?, ?)"
    data = (date_time, sensor_name, sensor_value, remark)
    
    myDB = MyDB()
    
    myDB.execute_insert_query(insert_query, data)

#------------------------------------------------------------------------------------------------------------------------

# creates list of SensorSimulator objects and set the attribute by fetching from config file (config.sensors)
def create_sensor_list():
    
    sensor_list = list()
    
    for sensor_name in config.sensors:
        data_rate = config.sensors[sensor_name]["data_rate"]
        trigger_value = config.sensors[sensor_name]["trigger_value"]
        trigger_data_rate = config.sensors[sensor_name]["trigger_data_rate"]
        amplitude = config.sensors[sensor_name]["amplitude"]
        noise_amp = config.sensors[sensor_name]["noise_amp"]
        signal_type = config.sensors[sensor_name]["signal_type"]
        remark = config.sensors[sensor_name]["remark"]
        
        sensorSimulator = SensorSimulator(sensor_name, data_rate, trigger_value, trigger_data_rate, amplitude, noise_amp, signal_type, remark)
        
        sensor_list.append(sensorSimulator)
    
    return sensor_list

#------------------------------------------------------------------------------------------------------------------------

def print_saved_data(date_time, sensor_name, sensor_value, remark):
    saved_data = {
        "date_time" : date_time,
        "sensor_name" : sensor_name,
        "sensor_value" : sensor_value,
        "remark" : remark
    }
    print(saved_data)
#------------------------------------------------------------------------------------------------------------------------

def print_database():
    query = "SELECT * FROM log ORDER BY id ASC"
    
    myDB = MyDB()
    
    result = myDB.execute_get_data_query(query)

    for row in result:
        print(row)
    
#------------------------------------------------------------------------------------------------------------------------

main()