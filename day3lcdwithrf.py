from RPLCD.i2c import CharLCD
lcd= CharLCD('PCF8574', 0x27)
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

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
        print(id)
        print(text)
        message()
        time.sleep(2)
finally:
    GPIO.cleanup()
