import pygame
import random
import math
def draw_lines1(screen):
    x=0
    while x<=640:
        x+=32
        pygame.draw.line(screen,"dark blue", (x,0),(x,512))
def draw_lines2(screen):
    y = 0
    while y <= 512:
        y += 32
        pygame.draw.line(screen, "dark blue", (0, y), (640, y))
def move_mole(screen, mole_image):
        position=screen.blit(mole_image,mole_image.get_rect(topleft=((random.randrange(0, 20) * 32), (random.randrange(0, 16) * 32))))
        return position

def range_of_mole(mole_position,mouse_space, spaces=16):
    mole_spot=(mole_position[0]+16,mole_position[1]+16)
    distance=math.hypot(mole_spot[0]-mouse_space[0],mole_spot[1]-mouse_space[1])
    return distance<=spaces

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        screen = pygame.display.set_mode((640, 512))
        mole_image = pygame.image.load("mole.png")
        testing=False
        mole_position=(0,0)

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if range_of_mole(mole_position,event.pos):
                        mole_position=move_mole(screen,mole_image)
            screen.fill("light green")
            draw_lines1(screen)
            draw_lines2(screen)
            screen.blit(mole_image,mole_position)


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
