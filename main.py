import glfw

from OpenGL.GL import *

def init():
    glClearColor(1,0.5,1,1)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(-0.6,0)
    glVertex2f(0.6,0)
    glVertex2f(0,0.3)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 1)
    glVertex2f(-0.6, -1)
    glVertex2f(0.6, -1)
    glVertex2f(0.6, 0)
    glVertex2f(-0.6, 0)
    glEnd()



def main():
    glfw.init()
    window = glfw.create_window(800, 600, 'Teste', None, None)
    glfw.make_context_current(window)
    init()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__" :
    main()
