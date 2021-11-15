from database.MyDB import MyDB

insert_query = "INSERT INTO `log` (`date_time`, `sensor_name`, `sensor_value`, `remark`) VALUES (?, ?, ?, ?)"
data = ("2021-11-13", "test", "50", "From python")

query = "SELECT * FROM log ORDER BY id ASC"

myDB = MyDB()
 
myDB.execute_insert_query(insert_query, data)

result = myDB.execute_get_data_query(query)

for x in result:
    print(x)