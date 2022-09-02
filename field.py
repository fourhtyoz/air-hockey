import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 600))
screen.fill('white')
pygame.display.update()


class Field:
    WIDTH = 1000
    HEIGHT = 600
    GREEN = (161,189,128)
    RED = (166,58,51)
    BLUE = (62,140,198)
    WHITE = (255, 255, 255)
    GREY = (43,41,41)
    def draw_blue_rect(self):
        self.rectangle = pygame.draw.rect(screen, self.BLUE, (0, 0, self.WIDTH//2, self.HEIGHT), 15)
    def draw_red_rect(self):
        self.rectangle = pygame.draw.rect(screen, self.RED, (self.WIDTH//2, 0, self.WIDTH//2, self.HEIGHT), 15)
    def draw_white_rect(self):
        self.rectangle = pygame.draw.rect(screen, self.WHITE, (15, 15, self.WIDTH - 30, self.HEIGHT - 30))
    def draw_circle_under_net(self):
        self.circle_left = pygame.draw.circle(screen, self.GREEN, (0, self.HEIGHT//2), 75)
        self.small_circle_left = pygame.draw.circle(screen, self.WHITE, (0, self.HEIGHT//2), 60)
        self.circle_right = pygame.draw.circle(screen, self.GREEN, (self.WIDTH, self.HEIGHT//2), 75)
        self.small_circle_right = pygame.draw.circle(screen, self.WHITE, (self.WIDTH, self.HEIGHT//2), 60)
    def draw_left_net(self):
        self.rectangle = pygame.draw.rect(screen, self.GREY, (0, self.HEIGHT//2-75, 15, 150))
    def draw_right_net(self):
        self.rectangle = pygame.draw.rect(screen, self.GREY, (self.WIDTH-15, self.HEIGHT//2-75, 15, 150))
    def draw_lines(self):
        self.line = pygame.draw.rect(screen, self.GREEN, (self.WIDTH//2-7.5, 15, 15, self.HEIGHT-30))
    def draw_circle(self):
        self.circle_left = pygame.draw.circle(screen, self.GREEN, (self.WIDTH//2, self.HEIGHT//2), 75)
        self.small_circle = pygame.draw.circle(screen, self.WHITE, (self.WIDTH//2, self.HEIGHT//2), 60)

class Joystick:
    RED_1 = (166,58,51)
    RED_2 = (128,0,0)
    BLUE_1 = (16,35,69)
    BLUE_2 = (62,140,198)
    def __init__(self):
        pass
    def draw_blue(self):
        self.base = pygame.draw.circle(screen, self.BLUE_1, (100, Field.WIDTH//2), 50)
        self.circle = pygame.draw.circle(screen, self.BLUE_2, (100, Field.WIDTH//2), 45)
    def draw_red(self):
        self.base = pygame.draw.circle(screen, self.RED_1, (Field.WIDTH - 200, 500), 50)
        self.circle = pygame.draw.circle(screen, self.RED_2, (100, Field.WIDTH//2), 45)


def draw_field(field, joystick):
    field.draw_blue_rect()
    field.draw_red_rect()
    field.draw_white_rect()
    field.draw_circle_under_net()
    field.draw_left_net()
    field.draw_right_net()
    field.draw_lines()
    field.draw_circle()
    joystick.draw_blue()
    joystick.draw_red()
    pygame.display.update()




def main():
    field = Field()
    joystick = Joystick()
    
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_field(field, joystick)
    pygame.quit()

if __name__ == '__main__':
    main()