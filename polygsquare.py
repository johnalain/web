#https://youtu.be/-YhddS9_uus?list=PLlvFEn0NKwXLjO-Wwm5MdNVDkXQnt4s3P&t=3113
from turtle import *

# pencil=Turtle()

# colors = ['red', 'green', 'lime green', 'yellow', 'orange', 'light blue']
# for i in range(6):
#     pencil.color= colors[i]
#     pencil.width(5)
#     pencil.fd(100)
#     pencil.rt(90)
# done()
from random import randint
pencil = Turtle()
for i in range(4):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color1 = (r/255, g/255, b/255)
x = randint(-200, 200)
y = randint(-200, 200)

pencil.up()
pencil.goto(x, y)
pencil.down()



pencil.color (color1)
pencil.begin_fill()
for i in range(4):
    pencil.fd(100)
    pencil.rt(90)
pencil.end_fill()

done()
    
    