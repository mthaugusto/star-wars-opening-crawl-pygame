import pygame
import time

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))

background_image = pygame.image.load("C:\\Users\\mthau\\Desktop\\Projetos\\Star-Wars-PyGame\\SW.png") 


# font_path = ("C:\\Users\\mthau\\Desktop\\starjedi\\Starjedi.ttf") 
font_size = 22
font = pygame.font.Font(None, font_size)
text_color = (255, 255, 0) 

crawl_text = [
    "EPISODE V",
    "THE EMPIRE STRIKES BACK",
    " ",
    "It is a dark time for the",
    "Rebellion. Although the Death",
    "Star has been destroyed,",
    "Imperial troops have driven the",
    "Rebel forces from their hidden", 
    "base and pursued them across",
    "the galaxy.",
    " ",
    "Evading the dreaded Imperial",
    "Starfleet, a group of freedom",
    "fighters led by Luke Skywalker",
    "has established a new secret",
    "base on the remote ice world of",
    "Hoth.",
    " ",
    "The evil lord Darth Vader,",
    "obsessed with finding young", 
    "Skywalker, has dispatched",
    "thousands of remote probes into",
    "the far reaches of space…",
]


text_x = width // 2
text_y = height

clock = pygame.time.Clock()



pygame.mixer.music.load("C:\\Users\\mthau\\Desktop\\Projetos\\Star-Wars-PyGame\\Star_Wars_Episodio_IV.mp3")
pygame.mixer.music.play()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(background_image, (0, 0))

    for i, line in enumerate(crawl_text):
        text_surface = font.render(line, True, text_color)
        text_rect = text_surface.get_rect(center=(text_x, text_y + (i * 40)))
        print(f"Line {i}: ({text_rect.x}, {text_rect.y})") # printando a posição da linha para verificação
        window.blit(text_surface, text_rect)

    
    text_y -= 1

    pygame.display.flip()
    clock.tick(60)
    time.sleep(0.04)

    if not pygame.mixer.music.get_busy():
        running = False

pygame.mixer.music.stop()
pygame.quit()