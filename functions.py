import pygame
import re



def initialise():
    window = pygame.display.set_mode((1280, 720))

    dialog = pygame.Surface((1180, 110))
    dialog.set_alpha(128)
    dialog.fill((0, 0, 0))

    controls = pygame.Surface((1180, 20))
    controls.set_alpha(128)
    controls.fill((0, 0, 0))

    pygame.font.init()
    dialog_font = pygame.font.SysFont('Arial', 20)

    return window, dialog, controls, dialog_font


def get_buttons():
    button1 = pygame.Surface((50, 10))
    button1.set_alpha(128)
    button1.fill((0, 0, 0))
    return 1


def render_text(line, surface, font, coords, color=(255, 255, 255), ):
    text_to_render = ''
    textsurface = None
    for i in line.line:
        text_to_render += i
        textsurface = font.render(text_to_render, False, color)
        surface.blit(textsurface, coords)
        pygame.display.update()
        pygame.time.wait(30)

    return textsurface


def save(line):
    with open('sf_file.txt', mode='w') as file:
        file.seek(0)
        file.write('last_line:{}'.format(line))

    return {
        'last_line': line
    }


def load_save():
    pattern1 = r'^last_line:([0-9]+)$'
    pattern1 = re.compile(pattern1)
    with open('sf_file.txt', mode='r') as file:
        last_line = re.findall(pattern1, file.read())

    return {
        'last_line': last_line
    }

