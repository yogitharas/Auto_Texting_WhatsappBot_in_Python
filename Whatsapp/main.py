import pyautogui as pt
from time import sleep
import pyperclip
import random


position1 = pt.locateOnScreen("Whatsapp/smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

def get_message():
    global x,y


    position = pt.locateOnScreen("Whatsapp/smiley_paperclip.png",confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y)
    pt.moveTo(x + 70, y - 40)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Received:" + whatsapp_message)
    return (whatsapp_message)

#posts
def postresponse(message):
    global x,y

    position = pt.locateOnScreen("Whatsapp/smiley_paperclip.png",confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200,y+20,duration=.5)
    pt.click()
    pt.typewrite(message,interval=.01)

    pt.typewrite("\n",interval=.01)

def process_response(message):
    random_no = random.randrange(3)
    hey = ["hey","hey!","heyyy"]
    hii = ["hii","hi","hai","hii!","hi!","hai!"]
    hlo = ["hlo","hello","hlo!","hello!"]
    food = ["coffee","cfe","milk","tea","dinner","break fast","lunch","coffee?","cfe?","milk?","tea?","dinner?","break fast?","lunch?"]
    wtdng = ["wat dng","what are you doing","en madthidhya","en madthidhya  ","en madthidhya "]
    whatsup = ["whats up","wassup","whatsup"]
    utta = ["utta","uta","Utta"]
    if str(message).lower() in hey:
        return "Hey!"

    else:
        if str(message).lower()  in hii:
            return "Hello!"
        elif str(message).lower() in hlo:
            return "Hii!"
        elif str(message).lower()  in food:
            return "had\nyou ?"
        elif str(message).lower() in wtdng:
            return "simply sitting"
        elif str(message).lower() in utta:
            return "aythu\nnindu ?"
        elif str(message).lower() in whatsup:
            return "Nothing"
        else:
            return "Hey!"

def check_for_new_messages():
    while True:
        try:
            position = pt.locateOnScreen("Whatsapp/unread.png",confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.move(-100,0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No new other users with nes messages located")

        if pt.pixelMatchesColor(int(x+70),int(y-40),(255,255,255),tolerance=10):
            processed_message = process_response(get_message())
            postresponse(processed_message)
        else:
            print("No new messages yt...")
        sleep(2)
check_for_new_messages()
#processed_message = process_response(get_message())
#postresponse(processed_message)
