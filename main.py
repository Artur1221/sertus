import pygame
import time
from backgrounds import *
from functions import *
from lines import *


running = True
paused = False

window, dialog, controls, dialog_font = initialise()
text_to_render = ''
text_surf = dialog_font.render(text_to_render, False, (255, 255, 255))

text_surf_arr = []

dbg_ctr = 0

text_ctr = 0

try:
    save_file = load_save()
except:
    save_file = save(0)

curr_line = int(save_file['last_line'][0])
curr_background = None
curr_line_obj = None

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

label_font = pygame.font.SysFont('Arial', 15)

label_surface_header = label_font.render('Dev Version', False, WHITE)
label_surface1 = label_font.render('S - save', False, WHITE)
label_surface2 = label_font.render('L - load', False, WHITE)

while running:
    curr_line_obj = lines[curr_line]

    curr_background = curr_line_obj.background
    window.blit(curr_background.image, curr_background.rect)

    window.blit(dialog, (50, 570))
    window.blit(controls, (50, 685))

    window.blit(label_surface_header, (10, 10))
    window.blit(label_surface1, (55, 686))
    window.blit(label_surface2, (110, 686))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                text_surf = render_text(curr_line_obj, window, dialog_font, (50 + 30, 570 + 10))

                curr_line += 1
                if curr_line == len(lines) - 1:
                    curr_line = -1

            if event.key == pygame.K_s:
                curr_line = int(save(curr_line)['last_line'])

            if event.key == pygame.K_l:
                curr_line = int(load_save()['last_line'][0])
                text_surf = render_text(curr_line_obj, window, dialog_font, (50 + 30, 570 + 10))

        if event.type == pygame.QUIT:
            running = False

    if curr_line_obj.to_postrender:
        window.blit(text_surf, (50 + 30, 570 + 10))

    pygame.time.wait(100)

    pygame.display.flip()


