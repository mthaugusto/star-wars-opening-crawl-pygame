import pygame
import time

# Initialize Pygame
pygame.init()

# Define the window dimensions
width, height = 800, 600
window = pygame.display.set_mode((width, height))

# Load the background image
background_image = pygame.image.load("C:\\Users\\mthau\\Desktop\\Projetos\\Star-Wars-PyGame\\SW.png")  # Replace with the path to your background image

# Define the font and text style
font_path = ("C:\\Users\\mthau\\Desktop\\starjedi\\Starjedi.ttf")  # Replace with the path to your Star Wars font file
font_size = 32
font = pygame.font.SysFont("freesansbold", font_size)
# font = pygame.font.Font(None, font_size) # 
text_color = (255, 255, 0)  # Yellow

# Define the crawl text
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

# Set up the clock
clock = pygame.time.Clock()


# Load and play the Star Wars theme music
pygame.mixer.music.load("C:\\Users\\mthau\\Desktop\\Projetos\\Star-Wars-PyGame\\Star_Wars_Episodio_IV.mp3")

pygame.mixer.music.play()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(background_image, (0, 0))

    # window.fill((0, 0, 0))  # Black - limpar o background 

    for i, line in enumerate(crawl_text):
        text_surface = font.render(line, True, text_color)
        text_rect = text_surface.get_rect(center=(text_x, text_y + (i * 40)))
        print(f"Line {i}: ({text_rect.x}, {text_rect.y})") # Verificador 
        window.blit(text_surface, text_rect)

    text_y -= 1

    pygame.display.flip()

    clock.tick(58)
    time.sleep(0.04)

    if not pygame.mixer.music.get_busy():
        running = False


pygame.mixer.music.stop()
pygame.quit()
