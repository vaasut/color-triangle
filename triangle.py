
#import basic OpenGL functionality
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *
import numpy as np

window_width = 500.0
window_height = 500.0

SIDE=250
HEIGHT=(sqrt(3) * SIDE) / 2.0

Ca=[1.0,0.0,0.0]
Cb=[0.0,1.0,0.0]
Cc=[0.0,0.0,1.0]

def initGL():

    glClearColor(0.0, 0.0, 0.0, 1.0)   #glClearColor( red , green , blue , alpha ), Specify the red, green, blue, and alpha values used when the color buffers are cleared
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(-window_width/2, window_width/2, -window_height/2, window_height/2)    #	reshape the window(double left, double right, double bottom, double top)


def triangle():
    """Creates an equilateral triangle centered at the origin of side length SIDE
    specified at top of program"""
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glVertex2f(0.0,HEIGHT/2)
    glVertex2f(SIDE/2,-HEIGHT/2)
    glVertex2f(-SIDE/2,-HEIGHT/2)
    glEnd()
    glFlush()


def side_func(x):
    """ returns the y-value for left and right sides of the triangle
     using a piecewise function. """
    y=(window_height-HEIGHT)/2.0 - sqrt(3) * (x-window_width/2.0)
    if (x>=250):
        y=(window_height-HEIGHT)/2.0 + sqrt(3) * (x-window_width/2.0)
    return y

def color_func(x,y):
    """Calculates the color that the triangle should be using a change of coordinates
    and rotation to make the math simple"""
    #change of coordinates
    x -= window_width/2
    y -= window_height/2

    fpac = (HEIGHT/2-y) # y distance between p and ac

    fpbc = (HEIGHT/2-sin(4*pi/3)*x-cos(4*pi/3)*y)#nearly the same, but include simple rotation

    beta = (fpac/HEIGHT)
    gamma = (fpbc/HEIGHT-.25) #subtract to correct range
    alpha= (1 - beta-gamma)

    Cx=[0.0,0.0,0.0]
    for i in range (3):
        Cx[i] = Ca[i] * alpha + Cb[i] *beta + Cc[i] * gamma
    #print Cx
    return Cx

def mouse(x,y):
    """ The mouse function uses the side_func to determine if the mouse 
    is inside or outside the triagle, and then if it is not outside it,
    it will use the color_func to determine color of the triangle"""

    if ( (y > (window_height+HEIGHT)/2) or (y < side_func(x)) ):
        glColor3f(1.0,1.0,1.0)
        triangle()

    else:
        colors=color_func(x,y)
        glColor3f(colors[0],colors[1],colors[2])
        triangle()


def main():
    """main function that intializes the window with a title
    and runs the display and mouse functions """
    glutInit(sys.argv)                        #initial the system
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)

    glutInitWindowSize(int(window_width), int(window_height))          #initial window size
    glutInitWindowPosition(100, 100)          #initial window position

    glutCreateWindow("ICSI 422 Demo")        #assign a title for the window


    initGL()

    glutDisplayFunc(triangle)
    glutPassiveMotionFunc(mouse)
    glutMainLoop()                           #callback function enter the GLUT event processing loop

if __name__ == "__main__":
    main()

