from turtle import *
shape('turtle')
speed(0.5)
def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)
triangle(sidelength=100)
for i in range(72):
    triangle(150)
    right(5)
    triangle(130)
    right(5)
    triangle(180)
  
  

  
