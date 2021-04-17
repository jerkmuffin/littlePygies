import pyglet
import random


window = pyglet.window.Window(1024, 868)
label = pyglet.text.Label("Dead Dog!",
                          font_name="Times New Roman",
                          font_size=36,
                          x=window.width//2, y=window.height - 50,
                          anchor_x='center', anchor_y='center')

image = pyglet.resource.image('sidsmall.jpg')
sound = pyglet.resource.media('Cat.mp3', streaming=False)
square = pyglet.shapes.Rectangle(x=(random.random() * window.width), y=(random.random() * window.height), width=200, height=200, color=(255, 0, 0))
fml = False


@window.event
def on_key_press(symbol, modifiers):
    print('a key was pressed: {} - {}'.format(symbol, modifiers))
    if symbol == pyglet.window.key.X:
        sound.play()

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    square.draw()
    label.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global fml
    print('button')
    fml = not fml




@window.event
def on_mouse_motion(x, y, dx, dy):
    # print("mouse is: {}, {}, {} , {}".format(x, y, dx, dy))
    window.clear()
    if fml:
        square.x = x
        square.y = y
    else:
        label.x = x
        label.y = y



pyglet.app.run()
