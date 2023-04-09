from adafruit_api import Adafruit_API
import time
from threading import Thread
from model import *
USERNAME = 'Heo_Rey'
KEY = 'aio_vjEe2384rWndxksf3C9kFmRumRwM'

def CheckStrawberryStatus(client):
    status = None
    counter = 0
    while True:
        if counter == 0:
            status = RunCamera()
            client.publish('strawberry-status',status[:-1])
            counter = 20
        counter-=1
        time.sleep(1)
feed_id_list = ['led','fan','pumper']

client = Adafruit_API(USERNAME, KEY, feed_id_list)
client.connect()
strawThread = Thread(target=CheckStrawberryStatus,args=[client])
strawThread.daemon = True
strawThread.start()
while(True):
    client.read_serial()
    time.sleep(1)