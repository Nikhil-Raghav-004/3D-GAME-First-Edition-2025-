import ursina
from ursina import *
import random

app = Ursina() #game screen initialization
EditorCamera(enabled=False)
camera_position = (0,5,-15)
camera_rotation_x = 20
camera_rotation_y = 20

Sky(color = color.orange)



ground = Entity(model = 'plane',  color = color.brown, scale = 10000, texture = 'brick',position = (0,-2,0), collider = 'box')

sphere = Entity(model = 'sphere',  color = color.blue, scale = 1, texture = 'shore', collider = 'sphere')

hurdles = []

for i in range(5):
    hurdles.append(
        Entity(
            model =  'cube',
            color = color.red,
            scale = (1,2,1),
            position =  (i *10 + 10, -1, 0),
            collider = 'box'
        )
    )

can_hit = True

velocity = 0
gravity =  - 0.03
bounce_strength = 0.1
move_Speed = 0.15

lives= 3

life_text = Text(
    text = f'Lives = {lives}',
    position = (-0.85, 0.45),
    scale  = 2
)



def update():
    global velocity
    global can_hit
    global lives

    velocity += gravity
    sphere.y += velocity

    # if sphere.y <= -1.5:
    #     sphere.y = 1.5
    #     velocity = -velocity * bounce_strength

    if sphere.y <= -1.5:
        sphere.y = -1.5
        velocity = 0

    if held_keys['d']:
        ground.x -= move_Speed
        for h in hurdles:
            h.x -= move_Speed


    if held_keys['a']:
        ground.x += move_Speed
        for h in hurdles:
            h.x += move_Speed
    for h in hurdles:
        if h.x < -10: #moving past the players
            h.x = random.randint(25,40) #respawn hurdles
            can_hit = True   


        if sphere.intersects(h).hit and can_hit:
            lives -= 1
            life_text.text = f"Lives : {lives}"
            can_hit = False

            if lives ==0:
                application.quit()


def input(key):
    global velocity
    global lives

    if key == 'space': # and  sphere.y <= -1.49:
        velocity = 0.25

    if key == 'escape':
        application.quit( )


app.run()
