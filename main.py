import explorerhat
from time import sleep
from bluedot import BlueDot
from signal import pause



speed = 100

def up():
    explorerhat.motor.one.forward(speed - 10)
    explorerhat.motor.two.forward(speed)
def down():
    explorerhat.motor.one.backward(speed)
    explorerhat.motor.two.backward(speed)
def left():
    explorerhat.motor.one.forward(speed / 2)
    explorerhat.motor.two.forward(speed)
def right():
    explorerhat.motor.one.forward(speed)
    explorerhat.motor.two.forward(speed / 2)
        
def off():
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def slider(pos):
  global speed  
  horizontal = ((pos.x + 1) / 2)
  percentage = round(horizontal * 100, 2)
  print("{}%".format(percentage))
  speed = percentage * 100


bd = BlueDot(cols=4, rows=3)
bd.color = "gray"
bd.square = True
bd.border = True

bd[0,0].visible = False
bd[2,0].visible = False
bd[0,2].visible = False
bd[2,2].visible = False
bd[1,1].visible = True



bd[1,0].when_pressed = up
bd[1,2].when_pressed = down
bd[0,1].when_pressed = left
bd[2,1].when_pressed = right
bd[1,1].when_pressed = off
bd[0,3].when_pressed = slider

pause()
