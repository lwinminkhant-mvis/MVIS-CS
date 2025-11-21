# from vpython import *

# scene = canvas(title="Mouse Example")

# # # Store the mouse object
# # mickey = scene.mouse

# # # Create a ball
# # ball1 = sphere(pos=vector(0,0,0), radius=0.4, color=color.red)

# # while True:
# #     rate(60)

# #     # getclick() pauses until a click happens
# #     click = mickey.getclick()
    
# #     # move ball to clicked position
# #     ball1.pos = click.pos


# from vpython import *

# scene = canvas(title="Drag Example")

# mickey = scene.mouse   # your format

# ball1 = sphere(pos=vector(0,0,0), radius=0.5, color=color.orange)

# dragging = False

# while True:
#     rate(120)

#     # Detect first click to start dragging
#     if mickey.events:
#         ev = mickey.getevent()
        
#         if ev.drag:      # started dragging
#             dragging = True
        
#         if ev.drop:      # released mouse
#             dragging = False

#     # While dragging, update ball position
#     if dragging:
#         ball1.pos = mickey.project(normal=vector(0,0,1))

from vpython import *
import random

scene.background = color.black
scene.title = "VPython 3x3 Rotating Objects Grid"
scene.width = 1024   # set to your screen width
scene.height = 768  # set to your screen height
scene.autoscale = True  # optional: automatically adjust camera to fit objects

# Setup objects to display
objects = []
rotation_speed = 0.01
colors = [color.blue, color.green, color.red, color.yellow, color.purple, color.orange, color.cyan, color.magenta]

for i in range(10):
    objects.append(box(pos=vector(random.randint(-5,5), random.randint(-5,5), random.randint(-5,5)), size=vector(2,2,1), color=random.choice(colors)))

# --- Click event handler ---
def hide_object(evt):
    print("removing object")
    obj = scene.mouse.pick
    if obj:
        obj.visible = False          # hide object
        if obj in objects:
            objects.remove(obj)      # optional: remove from rotation list

scene.bind('mouseup', hide_object)

# Rotation loop
while True:
    rate(100)
    for obj in objects:
        obj.rotate(angle=rotation_speed, axis=vector(1,1,1), origin=obj.pos)
