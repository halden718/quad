import time
from commandP import *

def cool():
    zero()
    all()
    time.sleep(3)
    zero()
    lift()
    forwards(150)
    time.sleep(2)
    backwards(175)
    time.sleep(1.5)
    for i in range (1,3):
      right(250-50*i)
      time.sleep(0.5*i)
      backwards(250-50*i)
      time.sleep(0.5*i)
      if i==2:
        down(100)
      else:
        up(100)
      sleep(0.5)
      left(250-50*i)
      time.sleep(0.5*i)
      forwards(250-50*i)
      time.sleep(0.5*i)
      
      
    for i in range (1,5):
        forward(200)
        time.sleep(0.3)
        backward(200)
        time.sleep(0.3)
    
      
def enter():
    zero()
    raw_input()
    all()
    raw_input()
    zero()
    up()
    raw_input()
    down()
    raw_input()
    all()
    raw_input()
    zero()
