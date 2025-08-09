# Turtle demo for Python-playground (copy into the editor to run in the browser)
#
# This script is intentionally simple so it works with Pyodide-based turtle
# implementations that map the standard `turtle` API to an SVG/canvas renderer.
#
# Usage:
# - Open the Python-playground in your browser
# - Create a new file and paste this script
# - Click "Run" to execute and observe the turtle drawing

import turtle
import time

screen = turtle.Screen()
screen.title("Python-playground Turtle Demo")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(5)
t.pensize(3)
t.color("steelblue")

# Draw a decorative square with corner stars
for i in range(4):
    t.forward(200)
    t.right(90)
    # draw a small star at the corner
    for _ in range(5):
        t.forward(20)
        t.right(144)
    t.penup()
    t.forward(40)
    t.pendown()
    t.backward(40)

# Move to center and draw a circle
t.penup()
t.goto(0, -50)
t.pendown()
t.color("tomato")
t.circle(50)

# Pause so the render can be observed (some playgrounds auto-close quickly)
try:
    time.sleep(2)
except:
    # time.sleep may not be available in some Pyodide environments; ignore if so
    pass

# End of demo
t.hideturtle()
screen.update()
