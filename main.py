#!/usr/bin/env python

import pygame
from pygame import locals

from block_handler import BlockHandler

import sys
from datetime import datetime

HELP_CONTENT = 'HELP-MENU\n' \
               '----------\n' \
               'Shortcuts:\n' \
               '\tf:\tToggle fullscreen\n' \
               '\tg:\tToggle mode (GM, Player)\n' \
               '\th:\tShow help menu\n' \
               '\tq,ESC:\tLeave\n' \
               '\tSPACE:\tMake screenshot\n' \
               ''


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    display = 800, 700
    fullscreen = False
    black = 0, 0, 0
    gray = 150, 150, 150
    gm_mode = False

    screen = pygame.display.set_mode(display)

    dd_map = pygame.image.load('map.jpg')
    dd_map = pygame.transform.scale(dd_map, display)

    block_handler = BlockHandler(display)
    block_group, all_blocks = block_handler.create_blocks()
    block_handler.set_default_block_positions()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == locals.KEYDOWN:
                    if event.key == locals.K_q or event.key == locals.K_ESCAPE:
                        sys.exit()

                    elif event.key == locals.K_f:
                        if not fullscreen:
                            screen = pygame.display.set_mode(display, pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode(display)
                        fullscreen = not fullscreen

                    elif event.key == locals.K_h:
                        print HELP_CONTENT
                    elif event.key == locals.K_SPACE:
                        pygame.image.save(screen, 'screenshot_%s.png' % str(datetime.now()))
                    elif event.key == locals.K_g:
                        if not gm_mode:
                            block_handler.remove_all_temporary()
                            gm_mode = True
                        else:
                            block_handler.restore_all_blocks()
                            gm_mode = False

            elif event.type == locals.MOUSEBUTTONDOWN:
                #print 'Mouseposition: %s' % str(pygame.mouse.get_pos())
                if not gm_mode:
                    block_handler.toggle_block(pygame.mouse.get_pos())

        screen.fill(black)
        screen.blit(dd_map, (0, 0))

        block_group.draw(screen)

        pygame.display.flip()
