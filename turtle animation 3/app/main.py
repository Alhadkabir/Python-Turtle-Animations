import turtle

t = turtle.Turtle()

# for animation speed
t.speed(0)

# for background color
turtle.bgcolor('black')

for i in range(240):
    t.color('cyan')
    t.circle(i)
    t.left(5)

# turtle end
turtle.done()