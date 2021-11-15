from database.MyDB import MyDB

def getData(last = 0):   
    query = "SELECT * FROM LOG"
    if(last != 0):
        query = query + " WHERE id > " + str(last)

    myDB = MyDB()
    result = myDB.execute_get_data_query(query)
    return str(result)