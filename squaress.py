import pyglet

window = pyglet.window.Window(1024, 768)

square1 = pyglet.shapes.Rectangle(x=0, y=0, width=window.width//2, height=window.height//2, color=(255, 0, 0))
square2 = pyglet.shapes.Rectangle(x=0, y=window.height//2, width=window.width//2, height=window.height//2, color=(0, 255, 0))
square3 = pyglet.shapes.Rectangle(x=window.width//2, y=0, width=window.width//2, height=window.height//2, color=(0,0,255))
square4 = pyglet.shapes.Rectangle(x=window.width//2, y=window.height//2, width=window.width//2, height=window.height//2, color=(66, 66, 66))
# i guess bottom left
@window.event
def on_draw():
    window.clear()
    square1.draw()
    square2.draw()
    square3.draw()
    square4.draw()


pyglet.app.run()
