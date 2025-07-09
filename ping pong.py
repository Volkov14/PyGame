import pygame
import random

pygame.init()

hight = 400
width = 600
SCREEN = pygame.display.set_mode((width, hight))
size_platform = 100


class Ball:
    def __init__(self, x, y, color=(255, 0, 0), speed=0.1):
        self.coordinate = [x, y]
        self.direction = [random.choice([-1, 1]), 1]
        self.color = color
        self.speed = speed
        self.ball_radius = 4
        self.rect = pygame.rect.Rect(x, y, self.ball_radius * 2, self.ball_radius * 2)

    def update(self):
        self.coordinate[0] += self.speed * self.direction[0]

        if 0 >= self.coordinate[0] or self.coordinate[0] >= width - self.ball_radius:
            self.direction[0] = -self.direction[0]

        self.coordinate[1] += self.speed * self.direction[1]

        if 0 >= self.coordinate[1]:
            self.direction[1] = -self.direction[1]

        self.rect.center = self.coordinate

    def draw(self):
        pygame.draw.circle(SCREEN, self.color, self.coordinate, self.ball_radius)


class Platform:
    def __init__(self, x, y, color=(255, 0, 0), speed=0.25):
        self.coordinate = [x, y]
        self.direction = [0, 0]
        self.color = color
        self.speed = speed
        self.height = 10
        self.width = 100
        self.rect = pygame.rect.Rect(x, y, self.width, self.height)

    def update(self):
        self.coordinate[0] += self.speed * self.direction[0]
        self.rect.center = self.coordinate

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self.rect)  # наложили рект на отрисовку вместе с платформой


class Game:
    def __init__(self):
        self.game_zone = []
        for x in range(0, width, 10):
            for y in range(0, int(hight/2), 10):
                self.game_zone.append(pygame.rect.Rect(x, y, 8, 8))

        self.platform = Platform(300, hight - 10)
        self.ball = Ball(width / 2, hight / 2 + 10)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_RIGHT:
                            self.platform.direction[0] = 1
                        case pygame.K_LEFT:
                            self.platform.direction[0] = -1
                elif event.type == pygame.KEYUP:
                    match event.key:
                        case pygame.K_RIGHT:
                            self.platform.direction[0] = 0
                        case pygame.K_LEFT:
                            self.platform.direction[0] = 0

            SCREEN.fill((0, 0, 0))
            self.update()
            self.draw()
            pygame.display.flip()

    def draw(self):
        for rect in self.game_zone:
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)
            if rect.colliderect(self.ball.rect):
                self.game_zone.remove(rect)
                self.ball.direction[1] = -self.ball.direction[1]
        self.platform.draw()
        self.ball.draw()

    def update(self):
        if self.platform.rect.colliderect(self.ball.rect):
            self.ball.direction[1] = -self.ball.direction[1]
        self.platform.update()
        self.ball.update()


game = Game()
game.run()
