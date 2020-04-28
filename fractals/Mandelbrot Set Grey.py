from graphics import *

#try : randomiser = -0.5 : y_offset = 1.114499259 : x_offset = 0.50015705
win_max = 200
scale = 100
y_offset = 0
x_offset = 0

#Create Graphics Window called "window" using size of win_max
win = GraphWin("window", win_max, win_max)

#iterate over size of graphics window
for num_y in range(0, win_max + 1):
    
    #We use this equation to get an offset and scale to the input of y
    y0 = (num_y/(scale)) - ((win_max/2)/scale) + y_offset

    #iterate again over size of graphics window for every pixel 200 * 200
    for num_x in range(0, win_max + 1):
            #We use this equation to get an offset and scale to the input of x
            x0 = (num_x/(scale)) - ((win_max/2)/scale) + x_offset
            iteration = 0
            max_iteration = 1000
            z = 0+0j
            ztemp = z
            while(abs(z) <4 and iteration < max_iteration):
                z = z**2 + (complex(x0, y0))
                # if the value hasn't changed since previous run then
                # leave the loop as it won't change
                if z == ztemp:
                    iteration = max_iteration
                    break
                ztemp = z
                iteration = iteration + 1
        #Use graphics Module to create a Point at x = num_x, y = num_y
            point = Point(num_x, num_y)
            r = ( iteration * 10 ) % 255
            g = iteration % 100
            b = iteration % 255
    
            if iteration == max_iteration:
                point.setFill("black")
            else:
                point.setFill(color_rgb(r,r,r))
            point.draw(win)
