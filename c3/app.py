import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def Prisma():
    vertices = (
        (-1, -1, 0),
        (-1, 1, 0),
        (1, -1, 0),
        (1, 1, 0),
        (0, 0, 1.5),
    )
    edges = (
        (0,1),
        (0,2),
        (0,4),
        (1,3),
        (1,4),
        (2,3),
        (2,4),
        (3,4),
    )
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (400,400)
    pygame.display.set_caption("Computação Gráfica")
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 1, 100.0)
    glTranslatef(0.0,0.0, -5)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        glRotatef(1, 1, 3, 3)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Prisma()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__=="__main__":
    main()
