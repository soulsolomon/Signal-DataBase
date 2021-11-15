from sensor.database.MySQLite import MySQLite


class MyDB(MySQLite):

    def __init__(self):
        super().__init__()

    def execute_get_data_query(self, query):
        DBResult = super().execute(query)
        result = list()
        try:
            for row in DBResult:
                result.append(row)
        except:
            print("Error: There is an error feting data from db.")
        finally:
            self.close_connection()
            return result
        
    def execute_insert_query(self, query, data):
        super().execute(query, data)
        self.close_connection()
    
    def close_connection(self):
        return super().close_connection()
        
        