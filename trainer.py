import time
import os

path = 'data/labelled/test.inf'

if(os.path.exists(path)):
    os.system("python -m stif_indonesia --exp-scenario supervised")
    os.remove(path)