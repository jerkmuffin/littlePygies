import pyglet
import random
import secrets
import glob
import json
import sys
import os

NUM = 85
if len(sys.argv) > 1:
    num = int(sys.argv[1])
else:
    num = NUM

window = pyglet.window.Window(1024, 768)
HEIGHT = window.height
WIDTH = window.width
picture = pyglet.resource.image('avatars/U01AE0JEC2C.png')
splim = pyglet.sprite.Sprite(picture)
splim.x = 0
splim.y = 0
from getData import getSlacky

colors = {"away": (255,0,0), "active":(0,255,0)}
get = getSlacky()
slackData = get.getUserInfo()
# slackData = secrets.slackData
print(json.dumps(slackData, indent=2))
num = len(slackData['members'])


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
                                               color = colors[slackData['members'][tag - 1]['profile']['isActive']])
            row['textbox_'
                + str(tag)] = pyglet.shapes.Rectangle(x=WIDTH/col * i,
                                                      y=y*HEIGHT/col,
                                                      width=WIDTH/col,
                                                      height=54,  # HEIGHT/col,
                                                      color=(0, 0, 0))

            row['label_'
                + str(tag)] = pyglet.text.Label(slackData['members'][tag - 1]['profile']['status_text'],
                                                font_name="Times New Roman",
                                                font_size=36,
                                                x=WIDTH/col*i+(WIDTH/col)/2,
                                                y=y*HEIGHT/col,# +(HEIGHT/col)/2,
                                                anchor_x='center',
                                                anchor_y='bottom')
            pic = glob.glob('avatars/' + slackData['members'][tag - 1]['id'] + '*')
            if pic:
                temp = pyglet.resource.image(pic[0])
                row['png_' + str(tag)] = pyglet.sprite.Sprite(temp)
                row['png_' + str(tag)].x = WIDTH/col * i + (((WIDTH/col) - (HEIGHT/col)) / 2)
                row['png_' + str(tag)].y = y*HEIGHT/col
                row['png_'
                    + str(tag)].scale = (HEIGHT/col)/row['png_' + str(tag)].height
    return row


def makeSquare(num):
    squares = {}
    div = getDims(num)
    for i in range(div):
        squares.update(makeARow(div, i, num))
    print(f"Squares: {squares.keys()}")
    print('squares are {} x {}.'.format(WIDTH/div, HEIGHT/div))
    # this is working for scaling || the height of the subsection devided by height of image to get a scale ratio
    splim.scale = (HEIGHT/div)/splim.height
    return squares


@window.event
def on_draw():
    squares = makeSquare(num)
    window.clear()
    for key in squares.keys():
        if 'label' not in str(key) and 'textbox' not in str(key):
            squares[key].draw()

    for key in squares.keys():
        if 'label' in str(key):
            squares[key].draw()
        if 'textbox' in str(key):
            squares[key].opacity = 125
            squares[key].draw()





pyglet.app.run()
