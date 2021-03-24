from RPLCD.i2c import CharLCD
lcd= CharLCD('PCF8574', 0x27)
import time


smiley = (
    
        0b00000,
        0b01010,
        0b01010,
        0b00000,
        0b10001,
        0b10001,
        0b01110,
        0b00000,
        )
sad =(
        0b00000,
        0b01010,
        0b01010,
        0b00000,
        0b01110,
        0b10001,
        0b10001,
        0b00000,
    )

happy =(
        0b00000,
        0b01010,
        0b01010,
        0b11111,
        0b10001,
        0b10001,
        0b01110,
        0b00000,
    )
bruh =(
        0b00000,
        0b01010,
        0b01010,
        0b00000,
        0b11111,
        0b11111,
        0b00000,
        0b00000,
    )
lcd.create_char(0, smiley)
lcd.create_char(1,sad)
lcd.create_char(2,happy)
lcd.create_char(3,bruh)




def border():
    lcd.cursor_pos = (0,0)
    lcd.write_string("\0******************\1")
    lcd.cursor_pos = (2,0)
    lcd.write_string("\2******************\3")
    lcd.cursor_pos = (3,0)
    lcd.write_string("====================")
    lcd.cursor_pos = (1,0)
    lcd.write_string("*")
    lcd.cursor_pos = (1,19)
    lcd.write_string("*")



x=""
while len(x)> 18 or len(x) == 0 :
    lcd.clear()
    lcd.write_string("Type the name")
    x=input()

border()
while True:
    lcd.cursor_pos = (1,1)
    lcd.write_string("                  ")
    time.sleep(1)
    
    
    width = (20-len(x))/2
    print(width)

    lcd.cursor_pos=(1,int(width))
    lcd.write_string(x)
    time.sleep(1)



