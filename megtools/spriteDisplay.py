import os
import sys
import pyglet
from PIL import Image

def sprite_show(path, name):
    image_format = name.split(sep='.')[-1]
    try:
        image = Image.open(path+'/'+name)
        image_width, image_height = image.size
        scale_factor = 300 / image_height
    except:
        return
    if image_format == 'gif':
        #pyglet does what we want it to do, but it's also the most retarded thing I've ever used.
        imgdir = [path]
        pyglet.resource.path=imgdir
        pyglet.resource.reindex()
        try:
            animation = pyglet.resource.animation(name)
            sprite = pyglet.sprite.Sprite(animation)
            sprite.update(scale=scale_factor)
            win = pyglet.window.Window(width=sprite.width, height=sprite.height)
            # set window background color = r, g, b, alpha
            # each value goes from 0.0 to 1.0
            green = 0, 1, 0, 1
            pyglet.gl.glClearColor(*green)
            @win.event
            def on_draw():
                win.clear()
                sprite.draw()
            @win.event
            def on_close():
                win.close()
                pyglet.app.exit()
            pyglet.app.run()
        finally:
            win.close()
    else:
        #pyglet does what we want it to do, but it's also the most retarded thing I've ever used.
        imgdir = [path]
        pyglet.resource.path=imgdir
        pyglet.resource.reindex()
        try:
            picture = pyglet.resource.image(name)
            sprite = pyglet.sprite.Sprite(picture)
            sprite.update(scale=scale_factor)
            win = pyglet.window.Window(width=sprite.width, height=sprite.height)
            # set window background color = r, g, b, alpha
            # each value goes from 0.0 to 1.0
            green = 0, 1, 0, 1
            pyglet.gl.glClearColor(*green)
            @win.event
            def on_draw():
                win.clear()
                sprite.draw()
            @win.event
            def on_close():
                win.close()
                pyglet.app.exit()
            pyglet.app.run()
        finally:
            win.close()
    return
