import mariadb

class MyMariaDB:
    
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        
        if(self.getDbConnection()):
            self.myCursor = self.myDBConn.cursor()
                            
    def getDbConnection(self):
        try:
            self.myDBConn = mariadb.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                port = int(self.port),
                database = self.database
            )

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return False
        else:
            return True

    def execute(self, query, data = ""):
        try:
            self.myCursor.execute(query, data)
        except:
            print(f"Error executing:")
        else:
            return self.myCursor
        
    def close_connection(self):
        #self.myCursor.close()
        pass
        
        
        