import pygame
from pygame import locals

import sys
import subprocess


class GameMenu(object):
    def __init__(self, screen, items, bg_color=(0, 0, 0), font=None, font_size=30,
                 font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

        self.chosen_map = None
        self.chosen_block_size = 100

        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)

            self.items.append([item, label, (width, height), (posx, posy)])

    def _prepare_menu_points(self, items):
        menu_points = []
        nr = 1
        for index, item in enumerate(items):
            label = self.font.render(str(nr) + '. ' + item, 1, self.font_color)
            nr += 1

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)

            menu_points.append([item, label, (width, height), (posx, posy)])
        return menu_points

    def chose_map(self):
        maps = subprocess.check_output(['ls', 'maps']).split()

        menu_points = self._prepare_menu_points(maps)

        choosing_map = True
        while choosing_map:
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == locals.KEYDOWN:
                    if event.key == locals.K_q or event.key == locals.K_ESCAPE:
                        sys.exit()
                        # 49 ^= 1
                    elif 49 <= event.key < (49 + len(menu_points)):
                        print event.key
                        key_index = event.key - 49
                        self.chosen_map = maps[key_index]
                        choosing_map = False

                        # Redraw the background
            self.screen.fill(self.bg_color)

            for name, label, (width, height), (posx, posy) in menu_points:
                self.screen.blit(label, (posx, posy))

            pygame.display.flip()

    def set_block_size(self):
        items = ['50', '100']
        menu_points =  self._prepare_menu_points(items)

        choosing_size = True
        while choosing_size:
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == locals.KEYDOWN:
                    if event.key == locals.K_q or event.key == locals.K_ESCAPE:
                        sys.exit()
                        # 49 ^= 1
                    elif event.key == locals.K_1:
                        self.chosen_block_size = 50
                        choosing_size = False
                    elif event.key == locals.K_2:
                        self.chosen_block_size = 100
                        choosing_size = False
                        # Redraw the background
            self.screen.fill(self.bg_color)

            for name, label, (width, height), (posx, posy) in menu_points:
                self.screen.blit(label, (posx, posy))

            pygame.display.flip()

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == locals.KEYDOWN:
                    if event.key == locals.K_q or event.key == locals.K_ESCAPE:
                        sys.exit()
                    elif event.key == locals.K_1:
                        # Chose map
                        self.chose_map()
                    elif event.key == locals.K_2:
                        # Select blocksize
                        self.set_block_size()
                    elif event.key == locals.K_3:
                        # Start
                        print 'Start'
                        if self.chosen_map:
                            mainloop = False

            # Redraw the background
            self.screen.fill(self.bg_color)

            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))

            pygame.display.flip()
