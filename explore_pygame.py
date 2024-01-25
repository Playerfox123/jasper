import pygame

fonts = pygame.font.get_fonts()

print(type(fonts))
for font in fonts:
    print (font)