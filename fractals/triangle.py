import graphics
import random

win = graphics.GraphWin("Window", 400, 400)
win.setBackground("white")
# this is a test
point_ax = 200
point_ay = 0
point_bx = 400
point_by = 400
point_cx = 0
point_cy = 400
new_pointx = 0
new_pointy = 0
count = 0
while count < 100000:
    point_to_go_to = random.randrange(3) + 1
    if point_to_go_to == 1:
        new_pointx = round(((point_ax - new_pointx) / 2) + new_pointx)
        new_pointy = round(((point_ay - new_pointy) / 2) + new_pointy)
    elif point_to_go_to == 2:
        new_pointx = round(((point_bx - new_pointx) / 2) + new_pointx)
        new_pointy = round(((point_by - new_pointy) / 2) + new_pointy)
    elif point_to_go_to == 3:
        new_pointx = round(((point_cx - new_pointx) / 2) + new_pointx)
        new_pointy = round(((point_cy - new_pointy) / 2) + new_pointy)
    point = graphics.Point(new_pointx, new_pointy)
    point.setFill("black")
    count = count + 1
    point.draw(win)
