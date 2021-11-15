from flask import Flask
from database.MyDB import MyDB

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    query = "SELECT * FROM LOG"
    
    myDB = MyDB()
    
    result = myDB.execute_get_data_query(query)

    
    return "<p>Hello, World 3!</p> " + str(result)