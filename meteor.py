import pygame
from pygame.sprite import Sprite


class Meteor(Sprite):
    """
    Uma classe que representa um meteoro
    """

    def __init__(self, ai_settings, screen):
        """
        Inicializa o meteoro em sua posição inicial
        """
        super(Meteor, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do meteoro
        self.image = pygame.image.load('images/meteor.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo meteoro próximo à parte superior esquerda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do meteoro
        self.x = float(self.rect.x)

    def blitme(self):
        """
        Desenha o meteoro em sua posição atual
        """
        self.screen.blit(self.image, self.rect)

