from flask import Flask
import mysql.connector
from RPLCD.i2c import CharLCD
lcd= CharLCD('PCF8574', 0x27)
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd="password",
    database ="attendance"
)

mycursor = mydb.cursor()
query = "Create table if not exists students(ID INT AUTO_INCREMENT PRIMARY KEY, RFID TEXT,Name TEXT, Time Datetime)"
mycursor.execute(query)







app = Flask(__name__)

@app.route("/")
def home():
    myhtml ='''
    <html>
        <head>
        <style>
        table, th, td {
          border: 1px solid black;
          border-collapse: collapse;
        }
        th, td {
          padding: 5px;
          text-align: left;    
        }
        </style>
        </head>
        <body>
        <h2>Student Attendace</h2>
        <table style="width:100%">
          <tr>
            <th>RFID</th>
            <th>Name</th>
            <th>Date</th>
          </tr>
'''
    sql="SELECT RFID,Name,Date_Format(time, '%Y-%m-%d %T.%f') FROM students limit 5;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
   
    
    for row in myresult:
        myhtml= myhtml+ '''
      <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
      </tr>
'''.format(row[0],row[1],row[2])
        print(row)
            
    myhtml = myhtml+'''
                </table>
                </body>
                </html>
            '''
        
            
    return myhtml

    
if __name__ == "__main__":
    app.run()