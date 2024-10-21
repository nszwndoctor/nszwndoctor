from turtle import *
shape('turtle')
speed(0.5)
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)
square(sidelength=100)
for i in range(3):
    square(50)
    right(5)
    square(30)
    right(5)
    square()
  
  
