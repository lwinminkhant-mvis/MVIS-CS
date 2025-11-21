from vpython import *
import os
os.system('cls' if os.name == 'nt' else 'clear')


b = box(pos = vec(0,0,0),size = vec(0.1,0.1,0.1) )

while True:
    rate(60)