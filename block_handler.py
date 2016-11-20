import pygame
from block import Block


class BlockHandler(object):
    def __init__(self, display_size):
        self.x = display_size[0]
        self.y = display_size[1]

        self.block_group = pygame.sprite.Group()
        self.all_blocks = []

        self.block_size = None

    def create_blocks(self, size=100):
        self.block_size = size

        number_of_blocks = (self.x / self.block_size) * (self.y / self.block_size)

        self.all_blocks = []
        for b in range(0, number_of_blocks):
            tmp = Block((0, 0, 0), self.block_size)
            self.block_group.add(tmp)
            self.all_blocks.append(tmp)
        return self.block_group, self.all_blocks

    def set_default_block_positions(self):
        x = 0
        y = 0

        for b in self.block_group:
            b.set_position(x, y)
            b.active = True
            x += self.block_size
            if x == self.x:
                x = 0
                y += self.block_size

    def toggle_block(self, mouse_position):
        click_x = mouse_position[0]
        click_y = mouse_position[1]

        for b in self.all_blocks:
            if (b.rect.x + self.block_size) > click_x >= b.rect.x:
                if (b.rect.y + self.block_size) > click_y >= b.rect.y:
                    if b.active:
                        self.block_group.remove(b)
                        b.active = False
                    else:
                        self.block_group.add(b)
                        b.active = True
                    break

    def remove_all_temporary(self):
        for b in self.block_group:
            self.block_group.remove(b)

    def restore_all_blocks(self):
        for b in self.all_blocks:
            if b.active:
                self.block_group.add(b)
