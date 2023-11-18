import os
import eel

from Features.PlaySound import *
from Body.Speak import *
# from Body.Listen import Listen
from main import *

eel.init("www")

playAssistantSound()



os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)
