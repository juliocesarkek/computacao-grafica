import pygame
from pygame.locals import *
from math import cos, sin

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def Sphere():
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    sphere = gluNewQuadric()
    gluQuadricDrawStyle(sphere, GLU_FILL)
    gluSphere(sphere, 1, 10, 10)
    glPopMatrix()

def main():
    pygame.init()
    display = (400,400)
    pygame.display.set_caption("Computação Gráfica")
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 1, 100.0)
    glTranslatef(0.0, 0.0, -5)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Sphere()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__=="__main__":
    main()
