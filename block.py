
import pygame


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, size=100):
        super(Block, self).__init__()
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        width = height = size

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        gray = 150, 150, 150
        border = 2
        pygame.draw.line(self.image, gray, (0, 0), (width, 0), border)
        pygame.draw.line(self.image, gray, (0, 0), (0, height), border)
        pygame.draw.line(self.image, gray, (width-border, 0), (width-border, height), border)
        pygame.draw.line(self.image, gray, (0, height-border), (width, height-border), border)

        self.active = None

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
