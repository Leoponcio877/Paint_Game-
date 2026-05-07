"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
import math

from turtle import (
    up, down, goto, color, begin_fill, end_fill,
    forward, left, right, circle as turtle_circle,
    setup, onscreenclick, listen, onkey, undo,
    speed, hideturtle, tracer, update
)	

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    radius = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    up()
    goto(start.x, start.y - radius)
    down()
    begin_fill()
    turtle_circle(radius)
    end_fill()
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = end.x - start.x
    height = end.y - start.y

    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()
    pass  # TODO


def triangle(start, end):
    """Dibuja un triángulo equilátero relleno.
 
    Calcula el lado del triángulo como la distancia entre 'start' y 'end'.
    El triángulo se dibuja con la base en la parte inferior, apuntando
    hacia arriba, centrado en 'start'.
 
    Args:
        start (vector): Vértice inferior izquierdo / punto de referencia (x, y).
        end   (vector): Punto que determina la longitud del lado (x, y).
 
    Returns:
        None
 
    Example:
        >>> triangle(vector(0, 0), vector(80, 0))  # lado = 80
    """
    side = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(3):
        forward(side)
        left(120)
    end_fill()
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
hideturtle()
speed(0)
tracer(False)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

update()

from turtle import done
done()
