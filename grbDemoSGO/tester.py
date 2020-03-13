import grb
from obj import *
from season_demo import *
from arcade import *

command = input("enter command here: ")
if command == "cu":
    exec("cutscene1()")
else:
    exec(command)