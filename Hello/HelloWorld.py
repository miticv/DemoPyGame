# Example of simple window and text that bounce or follow the mouse on the screen
import pygame, sys

#set up pygame
pygame.init()

#create GUI window
windowsSize = (800,600)
screen = pygame.display.set_mode(windowsSize)
pygame.display.set_caption("Simple demo")

#create font, use it to write sometning, and get its length
myriadProFont  = pygame.font.SysFont("Myriad Pro", 48)
helloWorld = myriadProFont.render("hello world", 1, (255,0,255), (255,255,255))
helloWorldSize = helloWorld.get_size()

#set up the clock to be consistent speed across different computers
clock = pygame.time.Clock()

x,y = 0,0
directionX, directionY = 1, 1
run = True

print("Game started")

while run:

    # close button on window GUID would not work unless we do this:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0,0,0))
    screen.blit(helloWorld, (x,y))


    if pygame.mouse.get_focused():
        mousePosition = pygame.mouse.get_pos()
        x, y = mousePosition
        if x + helloWorldSize[0] > 800:
            x = 800 - helloWorldSize[0]
        if y + helloWorldSize[1] > 600:
            y = 600 - helloWorldSize[1]
    else:
        x += 5 * directionX
        y += 5 * directionY
        if x + helloWorldSize[0] > 800 or x <= 0:
            directionX *= -1
        if y + helloWorldSize[1] > 600 or y <= 0:
            directionY *= -1


    # this draws the window on the screen
    pygame.display.update()
    # run 40 iterations per second:
    clock.tick(40) #40 frames per second


print("Game ended")
pygame.quit()
sys.exit()



