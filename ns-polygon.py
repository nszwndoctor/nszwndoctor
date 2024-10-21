from turtle import *
shape('turtle')
speed(0.5)
def polygon(sidelength=100):
    for i in range(8):
        forward(sidelength)
        right(45)
polygon(sidelength=100)
for i in range(6):
    polygon(100)
    right(5)  


  

