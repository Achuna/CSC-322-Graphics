import OpenGL
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

width, height = 500, 500  # window size

def triangle(x, y, width, height):
    glBegin(GL_POLYGON)
    glVertex2f(x, y)
    glVertex2f(x + width/2, y + height)
    glVertex2f(x + width, y)
    glEnd()

def line(x, y, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x2, y2)
    glEnd()

def square(x, y, height, width):
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_POLYGON) # Begin the sketch
    glVertex2f(x, y) # Coordinates for the bottom left point
    glVertex2f(x + width, y) # Coordinates for the bottom right point
    glVertex2f(x + width, y + height) # Coordinates for the top right point
    glVertex2f(x, y + height) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

def circle(x, y, radius):
    sides = 32
    radius = radius
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + x
        sine = radius * sin(i * 2 * pi / sides) + y
        glVertex2f(cosine, sine)
    glEnd()

def clouds(x, y):
    count = 0
    swap = True
    for i in range(0, 200):
        posx = x + i * 2
        if count == 10:
            count = 0
            swap = not swap
        else:
            count = count + 1
        if(swap):
            y = y + 10
        else:
            y = y - 10
        circle(posx, y, 10)
# Used to refresh our drawings so they don't disappear quickly
def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClearColor(0.0, 0.5, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen

    glLoadIdentity()  # Reset all graphic/shape's position
    refresh2d(width, height)

    #grass
    glColor3f(0.0, 1.0, 0.0)  # Set the color to pink
    square(0, 0, 100, 500)  # draw square using the function

    #house
    glColor3f(1.0, 0.5, 0.20)
    square(200, 100, 100, 100)  # draw square using the function

    #chimney
    glColor3f(0.0, 0.0, 0.0)
    square(265, 220, 50, 20)

    #roof
    glColor3f(0.7, 0.4, 1.0)
    triangle(200, 200, 100, 75)  # draw triangle using the function

    #door
    glColor3f(1.0, 1.0, 0.0)
    square(235, 100, 40, 30)

    #windows
    for i in range(0, 100, 50):
        square(215 + i, 160, 20, 20)

    #smoke
    glColor3f(1.0, 1.0, 1.0)
    circle(280, 280, 10)
    circle(285, 290, 15)

    #Sun
    glColor3f(1.0, 1.0, 0.0)
    circle(100, 450, 30)

    glColor3f(1, 1, 1)
    clouds(280, 280)

    glutSwapBuffers()   # important for double buffering


# initialization
glutInit()  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, height)  # set window size
glutInitWindowPosition(0, 0)  # set window position
wind = glutCreateWindow("CSC 322 Graphics HW1")  # create window with title
glutDisplayFunc(showScreen)  # set showScreen function callback
glutIdleFunc(showScreen)  # draw all the time
glutMainLoop()  # start everything
