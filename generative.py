import pyglet
import random
import sys

NUM = 85
if len(sys.argv) > 1:
    num = int(sys.argv[1])
else:
    num = NUM

window = pyglet.window.Window(1024, 768)
HEIGHT = window.height
WIDTH = window.width


def getDims(num):
    # limit of 100 sub-divisions???
    for i in range(16):
        if num <= i**2:
            return i
    print('too big for your britches')
    sys.exit()


def randomColor():
    return (int(random.random() * 255),
            int(random.random() * 255),
            int(random.random() * 255))


def makeARow(col, y, num):
    row = {}
    for i in range(col):
        tag = (i+1 + y*col)
        if tag > num:
            row[tag] = pyglet.shapes.Rectangle(x=WIDTH/col * i,
                                               y=y*HEIGHT/col,
                                               width=WIDTH/col,
                                               height=HEIGHT/col,
                                               color=(0, 0, 0))
        else:
            row[tag] = pyglet.shapes.Rectangle(x=WIDTH/col * i,
                                               y=y*HEIGHT/col,
                                               width=WIDTH/col,
                                               height=HEIGHT/col,
                                               color=randomColor())
            row['label_'
                + str(tag)] = pyglet.text.Label(str(tag),
                                                font_name="Times New Roman",
                                                font_size=36,
                                                x=WIDTH/col*i+(WIDTH/col)/2,
                                                y=y*HEIGHT/col+(HEIGHT/col)/2,
                                                anchor_x='center',
                                                anchor_y='center')
    return row


def makeSquare(num):
    squares = {}
    div = getDims(num)
    for i in range(div):
        squares.update(makeARow(div, i, num))
    print(f"Squares: {squares.keys()}")
    return squares


@window.event
def on_draw():
    squares = makeSquare(num)
    window.clear()
    for key in squares.keys():
        squares[key].draw()


pyglet.app.run()
