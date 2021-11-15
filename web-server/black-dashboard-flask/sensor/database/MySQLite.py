import sqlite3

class MySQLite:
    
    def __init__(self):
        self.myDBConn = None      
                            
    def getDbConnection(self):
        try:
            self.myDBConn = sqlite3.connect("..\\..\\sensor\\database\\datalogger.db")
            self.myCursor = self.myDBConn.cursor()
        except Exception as e:
            print(f"Error connecting to SQLite db.{e}")
            return False
        else:
            return True

    def execute(self, query, data = ""):
        
        self.getDbConnection()
        
        try:
            self.myCursor.execute(query, data)
            self.myDBConn.commit()
        except Exception as e:
            print(f"Error executing: {e}")
        else:
            return self.myCursor
        
    def close_connection(self):
        self.myCursor.close()

        