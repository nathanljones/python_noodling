from graphics import *

#generally use numbers between -1 and 1 for randomiser
#remember to change the window scale and offset

#try : randomiser = -0.5 : y_offset = 1.114499259 : x_offset = 0.50015705

randomiser = 0.5
precision = 100
win_max = 200
scale = 50
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

        #Initiate check and count for every pixel on the Graphics Window
        count = 0
        check = 0
        x = 0.0
        y = 0.0
                #We use this equation to get an offset and scale to the input of x
        x0 = (num_x/(scale)) - ((win_max/2)/scale) + x_offset
        iteration = 0
        max_iteration = 1000
        while ( x * x + y * y < 2 * 2 and iteration < max_iteration ):
            xtemp = x * x - y * y + x0
            y = 2 * x * y + y0
            x = xtemp
            iteration = iteration + 1
    
        #Use graphics Module to create a Point at x = num_x, y = num_y
        point = Point(num_x, num_y)
       
#This first value is used to colour the the standard Mandelbrot set black

        
        r = iteration * 10 % 50
        g = iteration % 100
        b = iteration % 255
        if iteration == max_iteration:
            point.setFill("black")
            
        elif iteration > 40:
            point.setFill("blue")           
            
        elif iteration > 32:
            point.setFill("cyan")
            
        elif iteration > 26:
            point.setFill("white")

        elif iteration > 18:
            point.setFill("yellow")

        elif iteration > 15:
            point.setFill("orange")    
            
        elif iteration > 12:
            point.setFill("red")
            
        elif iteration > 9:
            point.setFill("orange")
            
        elif iteration > 7:
            point.setFill("yellow")

        elif iteration > 6:
            point.setFill("white")
            
        elif iteration > 4:
            point.setFill("cyan")

        else:
            point.setFill("blue")

        
#        point.setFill(color_rgb(r,g,b))
        
        point.draw(win)
