import time

import pygame
import random

pygame.init()

hight = 400
width = 600
SCREEN = pygame.display.set_mode((width, hight))

size_turel = 30
size_alien = 30
size_bullet = 10


class Turel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.coordinate = [x, y]
        self.image = pygame.image.load('player.png').convert_alpha()  # конверт альфа включает фоновую прозрачность у
        # картинки
        self.image = pygame.transform.scale(self.image, (size_turel, size_turel))  # масштабирование картинки на экране
        self.rect = self.image.get_rect()  # обращается к катинки и по размеру создает рект

    def update(self):
        self.rect.center = self.coordinate
        keys = pygame.key.get_pressed()  # возвращает словарь где ключи все клавиши, а значения True или False: нажата или нет
        if keys[pygame.K_LEFT]:
            self.coordinate[0] -= 0.3
        elif keys[pygame.K_RIGHT]:
            self.coordinate[0] += 0.3

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.coordinate = [x, y]
        self.image = pygame.image.load('alien.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (size_alien, size_alien))
        self.rect = self.image.get_rect()
        self.direction = [random.choice([1, -1]), 1]
        self.speed = 0.02
        self.delay = random.randint(100,500)/35
        self.time_to_shoot = time.time()


    def update(self):
        self.rect.center = self.coordinate
        self.coordinate[0] += self.speed * self.direction[0]
        if 0 > self.coordinate[0] or self.coordinate[0] > width - size_alien:
            self.direction[0] = - self.direction[0]

    def check_reload(self):
        try_shoot = time.time()
        if try_shoot - self.time_to_shoot >= self.delay:
            self.time_to_shoot = try_shoot
            return True
        return False

class Game:
    def __init__(self):
        self.game = Turel(240, 360)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bullets_aliens = pygame.sprite.Group()
        self.turel = pygame.sprite.Group() # Создаём группу из 1 шт. turel

        for x in range(0, width - size_alien, 70):
            for y in range(size_alien, int(hight/2), 70):
                self.aliens.add(Alien(x, y))
        self.turel.add(self.game)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Alien_and_Turel_bullet(self.game.coordinate[0], self.game.coordinate[1] - size_turel//2, (200,200,200), 1)
                        self.bullets.add(bullet)

            for alien in self.aliens:
                if alien.check_reload():
                    bullet_alien = Alien_and_Turel_bullet(alien.coordinate[0], alien.coordinate[1], (200,240,240), -1)
                    self.bullets_aliens.add(bullet_alien)


            SCREEN.fill((0, 0, 0))
            self.update()
            self.draw()
            pygame.display.flip()

    def update(self):
        self.turel.update()
        self.aliens.update()
        self.bullets.update()
        self.bullets_aliens.update()
        for alien in self.aliens:
            for bullet in self.bullets:
                if bullet.rect.colliderect(alien.rect):
                    self.aliens.remove(alien)
                    self.bullets.remove(bullet)
        for bullet_alien in self.bullets_aliens:
            for bullet_gamer in self.bullets:
                if bullet_alien.rect.colliderect(bullet_gamer):
                    self.bullets_aliens.remove(bullet_alien)
                    self.bullets.remove(bullet_gamer)


    def draw(self):
        self.turel.draw(SCREEN) # у класса Group есть "встроенный метод draw и update"
        self.aliens.draw(SCREEN)
        self.bullets.draw(SCREEN)
        self.bullets_aliens.draw(SCREEN)

class Alien_and_Turel_bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color, direction):
        super().__init__()
        self.coordinate = [x, y]
        self.color = color
        self.direction = direction
        self.speed = 0.3
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (size_bullet/5, size_bullet))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = self.coordinate
        self.coordinate[1] -= self.speed * self.direction
        if self.coordinate[1] < 0 or self.coordinate[1] > hight:
            self.kill()




game = Game()
game.run()