import pygame

# constants
WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (14, 99, 37)
BLUE = (37, 16, 156)
ORANGE = (237, 219, 100)
LIGHTBLUE = (41, 138, 134)
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated human Robot")
width = 50
height = 30
line_width = 3
lower_arm_center_x = 540
lower_arm_center_y = 350
clock = pygame.time.Clock()
count = 0


# Function to animate the arm
def animate_arm():
    global count
    if 0 <= count <= 50:
        second_arm = pygame.Surface((50, 180))
        second_arm.fill(LIGHTBLUE)
        second_arm.set_colorkey(WHITE)
        second_arm_2 = pygame.transform.rotate(second_arm, -10)
        second_arm_rect2 = second_arm.get_rect()
        second_arm_rect2.center = (lower_arm_center_x, lower_arm_center_y)
        screen.blit(second_arm_2, second_arm_rect2)

        first_arm = pygame.Surface((50, 150))
        first_arm.fill(LIGHTBLUE)
        first_arm.set_colorkey(WHITE)
        first_arm_1 = pygame.transform.rotate(first_arm, 30)
        first_arm_rect1 = first_arm.get_rect()
        first_arm_rect1.center = (500, 225)
        screen.blit(first_arm_1, first_arm_rect1)

    if 50 <= count < 100:
        # This is the arm animation
        second_arm_anim = pygame.Surface((50, 180))
        second_arm_anim.fill(LIGHTBLUE)
        second_arm_anim.set_colorkey(WHITE)
        second_arm_anim_2 = pygame.transform.rotate(second_arm_anim, -120)
        second_arm_anim_rect2 = second_arm_anim.get_rect()
        second_arm_anim_rect2.center = (580, 350)
        screen.blit(second_arm_anim_2, second_arm_anim_rect2)

        first_arm = pygame.Surface((50, 150))
        first_arm.fill(LIGHTBLUE)
        first_arm.set_colorkey(WHITE)
        first_arm_1 = pygame.transform.rotate(first_arm, 30)
        first_arm_rect1 = first_arm.get_rect()
        first_arm_rect1.center = (500, 225)
        screen.blit(first_arm_1, first_arm_rect1)
    if count > 100:
        # This is the arm animation
        second_arm_anim = pygame.Surface((50, 180))
        second_arm_anim.fill(LIGHTBLUE)
        second_arm_anim.set_colorkey(WHITE)
        second_arm_anim_2 = pygame.transform.rotate(second_arm_anim, -180)
        second_arm_anim_rect2 = second_arm_anim.get_rect()
        second_arm_anim_rect2.center = (640, 160)
        screen.blit(second_arm_anim_2, second_arm_anim_rect2)

        first_arm = pygame.Surface((50, 150))
        first_arm.fill(LIGHTBLUE)
        first_arm.set_colorkey(WHITE)
        first_arm_1 = pygame.transform.rotate(first_arm, 70)
        first_arm_rect1 = first_arm.get_rect()
        first_arm_rect1.center = (500, 225)
        screen.blit(first_arm_1, first_arm_rect1)

    clock.tick(FPS)
    count += 1


# A function to display the normal arm
def normal_arm():
    first_arm = pygame.Surface((50, 150))
    first_arm.fill(LIGHTBLUE)
    first_arm.set_colorkey(WHITE)
    first_arm_1 = pygame.transform.rotate(first_arm, 30)
    first_arm_rect1 = first_arm.get_rect()
    first_arm_rect1.center = (500, 225)
    screen.blit(first_arm_1, first_arm_rect1)

    second_arm = pygame.Surface((50, 180))
    second_arm.fill(LIGHTBLUE)
    second_arm.set_colorkey(WHITE)
    second_arm_2 = pygame.transform.rotate(second_arm, -10)
    second_arm_rect2 = second_arm.get_rect()
    second_arm_rect2.center = (lower_arm_center_x, lower_arm_center_y)
    screen.blit(second_arm_2, second_arm_rect2)


# A function to draw the left arm
def left_arm_draw():
    # Drawing the arms
    third_arm = pygame.Surface((50, 200))
    third_arm.fill(LIGHTBLUE)
    third_arm.set_colorkey(WHITE)
    third_arm_3 = pygame.transform.rotate(third_arm, -20)
    third_arm_rect3 = third_arm.get_rect()
    third_arm_rect3.center = (180, 250)
    screen.blit(third_arm_3, third_arm_rect3)
    # Drawing the arms
    fourth_arm = pygame.Surface((50, 200))
    fourth_arm.fill(LIGHTBLUE)
    fourth_arm.set_colorkey(WHITE)
    fourth_arm_4 = pygame.transform.rotate(fourth_arm, 6)
    fourth_arm_rect4 = fourth_arm.get_rect()
    fourth_arm_rect4.center = (180, 420)
    screen.blit(fourth_arm_4, fourth_arm_rect4)


# A function to draw the legs
def leg_draw():
    first_leg = pygame.Surface((70, 350))
    first_leg.fill(BLUE)
    first_leg.set_colorkey(WHITE)
    first_leg_1 = pygame.transform.rotate(first_leg, -10)
    first_leg_rect1 = first_leg.get_rect()
    first_leg_rect1.center = (240, 545)
    screen.blit(first_leg_1, first_leg_rect1)
    # Drawing the legs
    second_leg = pygame.Surface((70, 350))
    second_leg.fill(BLUE)
    second_leg.set_colorkey(WHITE)
    second_leg_2 = pygame.transform.rotate(second_leg, 10)
    second_leg_rect2 = second_leg.get_rect()
    second_leg_rect2.center = (450, 545)
    screen.blit(second_leg_2, second_leg_rect2)


# Function to display the starting text
start_text = pygame.font.Font("freesansbold.ttf", 20)


def display_text(x, y):
    start = start_text.render("Long press 'A' to animate:", True, (0, 0, 0))
    screen.blit(start, (x, y))


# Beginning of the man game window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if count > 110:
                count = 0
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    # Displaying the start text
    display_text(10, 10)
    # Drawing the head
    X, Y, radius, width = 380, 80, 70, 2
    pygame.draw.circle(screen, BLACK, (X, Y), radius, width)
    X, Y, radius = 380, 80, 65
    pygame.draw.circle(screen, ORANGE, (X, Y), radius)
    # Drawing the body
    X, Y, width, height = 250, 160, 250, 250
    pygame.draw.rect(screen, GREEN, (X, Y, width, height))
    # Drawing the arms
    # Drawing and animating the arm
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        animate_arm()
    else:
        normal_arm()
    # Drawing the second arm
    left_arm_draw()
    # Drawing the legs
    leg_draw()
    pygame.display.update()
pygame.quit()
