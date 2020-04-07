import turtle

def star(color, sides, length, angle, distance, width, speed):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(width)  # visible!
    galileo.speed(speed)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star
   
for angle in [180, 135, 90, 45, 0, -45, -90, -135]:
    star("red", 5, 50, angle, 100, 8, 0)
    
for angle in [180, 135, 90, 45, 0, -45, -90, -135]:
    star ("blue", 5, 25, angle, 50, 5, 0)
