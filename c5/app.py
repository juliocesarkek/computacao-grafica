import pygame
from pygame.locals import *
from math import cos, sin, pi

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def functionFxy(x, y):
    return 0.5 * sin(pi * x / 10) * cos(pi * y / 10)

def mesh():
    r = 10
    vertices = []
    faces = []

    for i in range(r):
        for j in range(r):
            vertices.append([i / r - 0.5, j / r - 0.5, functionFxy(j + r / 2, i + r)])

    for vertexIndex in range(len(vertices)):
        if vertexIndex % r == 0:
            continue
        if vertexIndex / r > r - 1:
            continue
        vertexIndex = vertexIndex - 1
        faces.append([vertexIndex, vertexIndex + r, vertexIndex + 1])
        faces.append([vertexIndex + 1, vertexIndex + r + 1, vertexIndex + r])

    glPushMatrix()
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    for face in faces:
        glVertex(vertices[face[0]])
        glVertex(vertices[face[1]])
        glVertex(vertices[face[2]])
    glEnd()
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
        mesh()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__=="__main__":
    main()
