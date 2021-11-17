from sensor.database.MyDB import MyDB

def getData(sensorName, last = 0):   
    query = "SELECT id, date_time, sensor_value FROM LOG WHERE sensor_name = '" + sensorName + "'"
    if(last != 0):
        query = query + " AND id > " + str(last)

    myDB = MyDB()
    result = myDB.execute_get_data_query(query)
    return result

def getDistinctSensors():
    query = "SELECT DISTINCT sensor_name FROM LOG"
    myDB = MyDB()
    result = myDB.execute_get_data_query(query)
    return result

def getLogData(last_id = 0):
    query = "SELECT date_time, sensor_name, sensor_value FROM LOG WHERE id > " + str(last_id)
    
    myDB = MyDB()
    result = myDB.execute_get_data_query(query)
    return result