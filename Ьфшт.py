import pygame

# pygame.init()
# surface = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
# pygame.display.set_caption("Первая игра")
#
# clock = pygame.time.Clock()
# FPS = 60
#
# pygame.draw.rect(surface, (255, 0, 0), (10, 10, 100, 30))
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#     clock.tick(FPS)


pygame.init()
SURFACE = pygame.display.set_mode((600, 400), pygame.RESIZABLE)


class Figure:

    def __init__(self, size_, x, y, color=(255, 0, 0), speed=0.25):
        self.size_ = size_
        self.coordinate = [x, y]
        self.direction = [0, 0]
        self.color = color # тут ранее было прописано значение по умолчанию. Я думаю, что в этом была мини-ошибка
        self.speed = speed
    def draw(self):
        pygame.draw.rect(SURFACE, self.color, (*self.coordinate, self.size_, self.size_))

    def update(self):
        self.coordinate[0] += self.speed * self.direction[0]
        self.coordinate[1] += self.speed * self.direction[1]

class Game:
    def __init__(self):
        self.square = Figure(30, 10, 10)

    def run(self):
        while True:
            """
            1)обработка события ивентов в цикле
            2)обновление объекта
            3)отрисовка объектов
            
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_RIGHT:
                            self.square.direction[0] = 1
                        case pygame.K_LEFT:
                            self.square.direction[0] = -1
                        case pygame.K_UP:
                            self.square.direction[1] = -1
                        case pygame.K_DOWN:
                            self.square.direction[1] = 1
                elif event.type == pygame.KEYUP:
                    match event.key:
                        case pygame.K_RIGHT:
                            self.square.direction[0] = 0
                        case pygame.K_LEFT:
                            self.square.direction[0] = 0
                        case pygame.K_UP:
                            self.square.direction[1] = 0
                        case pygame.K_DOWN:
                            self.square.direction[1] = 0

            self.update()

            SURFACE.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def draw(self):
        self.square.draw()

    def update(self):
        self.square.update()

game = Game()
game.run()
