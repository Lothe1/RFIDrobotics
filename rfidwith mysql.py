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



def message():
    lcd.write_string("Welcome, "+ text)
    lcd.cursor_pos =(1,0)
    lcd.write_string("id: "+str(id))
    
def greetingmsg():
    lcd.write_string("Scan you id lah smol brain dingdong")



try: 
    while True:
        lcd.clear()
        greetingmsg()
        id, text = reader.read()
        lcd.clear()
        message()
        
        sql= "INSERT INTO students(RFID, Name, Time) VALUES  (%s,%s,now());"
        val = (str(id), text)
        mycursor.execute(sql, val)
        mydb.commit()
        
        sql="SELECT RFID,Name,Date_Format(time, '%Y-%m-%d %T.%f') FROM students;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        
        for row in myresult:
            print(row)
        time.sleep(2)
finally:
    GPIO.cleanup()