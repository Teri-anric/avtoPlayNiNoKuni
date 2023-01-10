from time import sleep
from pyautogui import  write,  click, Point #,hotkey,press

#constant point
select_server = Point(900, 830)
email_textInput = Point(900, 450)
password_textInput = Point(900, 500)
login_button = Point(900, 666)
start_button = (1600, 1000)
start_game_button = Point(1500, 900)



def start_game():
    hotkey("win", "s")
    write("Netmarble Launcher")
    press("enter")
    press("enter")
    sleep(8)
    click(start_game_button)


def login(email: str, password:str):
    click(*select_server)
    write_email(email)
    write_pasword(password)
    click(login_button)
    sleep(10)
    click()
    sleep(50)
    click(start_button)


def write_email(email: str):
    click(email_textInput)
    write(email, interval=0.1)
    
def write_pasword(password: str):
    click(password_textInput)
    write(password, interval=0.1)




