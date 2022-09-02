import pygame

pygame.init()

#Settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
PADDLE = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (43,41,41)
SCORE_COLOR = (38,30,11)
WINNING_SCORE = 10

SCORE_FONT = pygame.font.SysFont('Arial', 40, True)
WIN_FONT = pygame.font.SysFont('Arial', 70, True)

VERSION = 0.1
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"Air Hockey v. {VERSION}")

def draw(screen, field, left_net, right_net, puck, left_stick, right_stick, right_score, left_score):
    field.draw_blue_rect()
    field.draw_red_rect()
    field.draw_white_rect()
    field.draw_circle_under_net()
    left_net.left_net()
    right_net.right_net()
    field.draw_lines()
    field.draw_circle()

    puck.draw(screen)
    left_stick.draw_left(screen)
    right_stick.draw_right(screen)

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, SCORE_COLOR)
    right_score_text= SCORE_FONT.render(f"{right_score}", 1, SCORE_COLOR)
    screen.blit(left_score_text, (SCREEN_WIDTH//2 - 40, 20))
    screen.blit(right_score_text, (SCREEN_WIDTH//2 + 20, 20))

    pygame.display.update()

class Field:
    GREEN = (161,189,128)
    RED = (166,58,51)
    BLUE = (62,140,198)
    WHITE = (255, 255, 255)
    GREY = (43,41,41)
    def draw_blue_rect(self):
        pygame.draw.rect(screen, self.BLUE, (0, 0, SCREEN_WIDTH//2, SCREEN_HEIGHT), 15)
    def draw_red_rect(self):
        pygame.draw.rect(screen, self.RED, (SCREEN_WIDTH//2, 0, SCREEN_WIDTH//2, SCREEN_HEIGHT), 15)
    def draw_white_rect(self):
        pygame.draw.rect(screen, self.WHITE, (15, 15, SCREEN_WIDTH - 30, SCREEN_HEIGHT - 30))
    def draw_circle_under_net(self):
        pygame.draw.circle(screen, self.GREEN, (0, SCREEN_HEIGHT//2), 75)
        pygame.draw.circle(screen, self.WHITE, (0, SCREEN_HEIGHT//2), 60)
        pygame.draw.circle(screen, self.GREEN, (SCREEN_WIDTH, SCREEN_HEIGHT//2), 75)
        pygame.draw.circle(screen, self.WHITE, (SCREEN_WIDTH, SCREEN_HEIGHT//2), 60)
    def draw_left_net(self):
        self.left_net = pygame.draw.rect(screen, self.GREY, (0, SCREEN_HEIGHT//2-75, 15, 150))
    def draw_right_net(self):
        self.right_net = pygame.draw.rect(screen, self.GREY, (SCREEN_WIDTH-15, SCREEN_HEIGHT//2-75, 15, 150))
    def draw_lines(self):
        pygame.draw.rect(screen, self.GREEN, (SCREEN_WIDTH//2-7.5, 15, 15, SCREEN_HEIGHT-30))
    def draw_circle(self):
        pygame.draw.circle(screen, self.GREEN, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), 75)
        pygame.draw.circle(screen, self.WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), 60)
        pygame.draw.circle(screen, self.RED, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), 15)

class Net:
    def left_net(self):
        self.x = 0
        self.y = SCREEN_HEIGHT//2-75
        self.height = 150
        self.left = pygame.draw.rect(screen, GREY, (self.x, self.y, 15, self.height))
    def right_net(self):
        self.x = SCREEN_WIDTH-15
        self.y = SCREEN_HEIGHT//2-75
        self.height = 150
        self.right = pygame.draw.rect(screen, GREY, (self.x, self.y, 15, self.height))

class Puck:
    VELOCITY = 10
    RADIUS = 15
    GREY_2 = (188,183,166)
    GREY_1 = (43,41,41)
    def __init__(self, x, y):
        self.x = self.original_x = x 
        self.y = self.original_y = y
        self.radius = self.RADIUS
        self.x_vel = self.VELOCITY
        self.y_vel = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.GREY_2, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= 1
        
class Stick:
    VELOCITY = 20
    RED_1 = (204, 0, 0)
    RED_2 = (102, 0, 0)
    RED_3 = (255, 0, 0)
    BLUE_1 = (0, 102, 204)
    BLUE_2 = (0, 51, 102)
    BLUE_3 = (0, 128, 255)
    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.left = True

    def draw_left(self, screen):
        pygame.draw.circle(screen, self.BLUE_1, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, self.BLUE_2, (self.x, self.y), 20)
        pygame.draw.circle(screen, self.BLUE_3, (self.x, self.y), 10)
    
    def draw_right(self, screen):
        pygame.draw.circle(screen, self.RED_1, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, self.RED_2, (self.x, self.y), 20)
        pygame.draw.circle(screen, self.RED_3, (self.x, self.y), 10)

    def move(self, up=True):
        if up:
            self.y += self.VELOCITY
        else:
            self.y -= self.VELOCITY

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

def handle_stick_movement(keys, left_stick, right_stick):
    if keys[pygame.K_w] and left_stick.y >= PADDLE + 50:
        left_stick.y -= left_stick.VELOCITY
    if keys[pygame.K_s] and left_stick.y <= SCREEN_HEIGHT - PADDLE - 40:
        left_stick.y += left_stick.VELOCITY
    if keys[pygame.K_a] and left_stick.x >= PADDLE + 30:
        left_stick.x -= left_stick.VELOCITY
    if keys[pygame.K_d] and left_stick.x <= SCREEN_WIDTH//2 - 50:
        left_stick.x += left_stick.VELOCITY

    if keys[pygame.K_UP] and right_stick.y >= PADDLE + 50:
        right_stick.y -= right_stick.VELOCITY
    if keys[pygame.K_DOWN] and right_stick.y <= SCREEN_HEIGHT - PADDLE - 40:
        right_stick.y += right_stick.VELOCITY
    if keys[pygame.K_RIGHT] and right_stick.x <= SCREEN_WIDTH - PADDLE - 30:
        right_stick.x += right_stick.VELOCITY
    if keys[pygame.K_LEFT] and right_stick.x >= SCREEN_WIDTH//2 + 50:
        right_stick.x -= right_stick.VELOCITY
    
def handle_hits(puck, left_stick, right_stick):
    vector1 = pygame.math.Vector2(puck.x, puck.y) #Puck
    vector2 = pygame.math.Vector2(left_stick.x, left_stick.y) #Left joystick
    vector3 = pygame.math.Vector2(right_stick.x, right_stick.y) #Right joystick
    
    if puck.x_vel < 0:
        if vector1.distance_to(vector2) < puck.radius + left_stick.radius:
            puck.x_vel *= -1

            middle_y = left_stick.y + left_stick.radius
            difference_in_y = middle_y - puck.y
            reduction_factor = (left_stick.radius) / puck.VELOCITY
            y_vel = difference_in_y / reduction_factor
            puck.y_vel = -1 * y_vel
    else:
        if vector1.distance_to(vector3) < puck.radius + right_stick.radius:
            puck.x_vel *= -1

            middle_y = right_stick.y + right_stick.radius
            difference_in_y = middle_y - puck.y
            reduction_factor = (right_stick.radius) / puck.VELOCITY
            y_vel = difference_in_y / reduction_factor
            puck.y_vel = -1 * y_vel

def handle_collisions(puck):
    if puck.y + puck.radius >= SCREEN_HEIGHT:
        puck.y_vel *= -1
    elif puck.y - puck.radius <= 0:
        puck.y_vel *= -1

    if puck.x <= 0:
        if puck.y + puck.radius <= SCREEN_HEIGHT//2 - 75:
            puck.x_vel *= -1
        elif puck.y + puck.radius >= SCREEN_HEIGHT//2 + 75:
            puck.x_vel *= -1
    elif puck.x >= SCREEN_WIDTH: 
        if puck.y + puck.radius >= SCREEN_HEIGHT//2 + 75:
            puck.x_vel *= -1
        elif puck.y + puck.radius <= SCREEN_HEIGHT//2 - 75:
            puck.x_vel *= -1

def main():
    clock = pygame.time.Clock()
    puck = Puck(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    left_stick = Stick(0, (SCREEN_HEIGHT//2), 30)
    right_stick = Stick(SCREEN_WIDTH, (SCREEN_HEIGHT//2), 30)

    field = Field()
    
    left_net = Net()
    right_net = Net()
    
    left_score = 0
    right_score = 0
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        #Scoring:
        if puck.x < 0:
            right_score += 1
            puck.reset()
        elif puck.x > SCREEN_WIDTH:
            left_score += 1
            puck.reset()
        
        win = False
        if right_score >= WINNING_SCORE:
            win_text = "Right player won"
            win = True

        elif left_score >= WINNING_SCORE:
            win_text = "Left player won"
            win = True
        if win:
            text = WIN_FONT.render(win_text, 1, SCORE_COLOR)
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2-text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            puck.reset()
            left_stick.reset()
            right_stick.reset()
            left_score = 0
            right_score = 0

        puck.move()
        handle_stick_movement(keys, left_stick, right_stick)
        handle_hits(puck, left_stick, right_stick)
        handle_collisions(puck)
        draw(screen, field, left_net, right_net, puck, left_stick, right_stick, right_score, left_score)
    
    pygame.quit()

if __name__ == "__main__":
    main()




