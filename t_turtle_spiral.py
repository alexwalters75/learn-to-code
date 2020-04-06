import turtle

def spiral(sides, turn, color, width, speed):
    t = turtle.Turtle()
    t.speed(speed)
    t.color(color)
    t.width(width)
    for n in range(sides):
        t.forward(n)
        t.right(turn)

spiral(200, 75, "cyan", 2, 0)
