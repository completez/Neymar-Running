import pygame
import sys
import random
import os

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEYMAR RUNNING")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
FONT = pygame.font.SysFont(None, 55)
SMALL_FONT = pygame.font.SysFont(None, 35)

player_img = None
config_file = "config.txt"

player_x = 100
player_y = HEIGHT - 150
player_width, player_height = 50, 50
gravity = 0.5
jump_speed = 0
jump_count = 0
is_jumping = False
MAX_JUMPS = 2

obstacle_width, obstacle_height = 40, 60
obstacles = []
coin_size = 20
coins = []
scroll_speed = 5
score = 0

is_logged_in = False
username = ''
password = ''
active_input = 'username'
input_color_active = (0, 0, 255)
input_color_inactive = (200, 200, 200)
input_color = input_color_inactive
error_message = ''
correct_username = "user"
correct_password = "pass"

def load_config():
    global player_img
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            img_file = f.readline().strip()
            if os.path.exists(img_file):
                player_img = pygame.image.load(img_file)
                player_img = pygame.transform.scale(player_img, (50, 50))
                print(f"Loaded image from config: {img_file}")
            else:
                print("Image file not found, please input a valid image.")
                input_image_file()
    else:
        input_image_file()

def input_image_file():
    global player_img
    img_file = input("Enter image filename (e.g., 'neymar.png'): ")
    if os.path.exists(img_file):
        player_img = pygame.image.load(img_file)
        player_img = pygame.transform.scale(player_img, (50, 50))
        with open(config_file, 'w') as f:
            f.write(img_file)
        print(f"Image saved to config: {img_file}")
    else:
        print("Image file not found. Please try again.")
        input_image_file()

def create_obstacle():
    obstacle_x = WIDTH + random.randint(100, 300)
    obstacles.append([obstacle_x, HEIGHT - obstacle_height - 50])

def create_coin():
    coin_x = WIDTH + random.randint(100, 300)
    coin_y = random.randint(100, HEIGHT - 100)
    coins.append([coin_x, coin_y])

def login_screen():
    global username, password, active_input, input_color, error_message
    screen.fill(WHITE)
    
    text_surface = FONT.render("Login", True, BLACK)
    screen.blit(text_surface, (WIDTH // 2 - 50, 50))
    
    username_rect = pygame.Rect(WIDTH // 2 - 100, 150, 200, 50)
    password_rect = pygame.Rect(WIDTH // 2 - 100, 250, 200, 50)

    pygame.draw.rect(screen, input_color if active_input == 'username' else input_color_inactive, username_rect, 2)
    pygame.draw.rect(screen, input_color if active_input == 'password' else input_color_inactive, password_rect, 2)
    
    username_surface = FONT.render(username, True, BLACK)
    password_surface = FONT.render('*' * len(password), True, BLACK)
    screen.blit(username_surface, (username_rect.x + 10, username_rect.y + 10))
    screen.blit(password_surface, (password_rect.x + 10, password_rect.y + 10))
    
    if error_message:
        error_surface = SMALL_FONT.render(error_message, True, RED)
        screen.blit(error_surface, (WIDTH // 2 - 100, 350))
    
    pygame.display.update()
    return username_rect, password_rect

def game_screen():
    global player_y, is_jumping, jump_speed, jump_count, score
    
    screen.fill(WHITE)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and jump_count < MAX_JUMPS:
        is_jumping = True
        jump_speed = -10  
        jump_count += 1

    if is_jumping:
        player_y += jump_speed  
        jump_speed += gravity  

        if player_y >= HEIGHT - 150:
            player_y = HEIGHT - 150
            is_jumping = False  
            jump_count = 0  
            jump_speed = 0  

    for obstacle in obstacles:
        obstacle[0] -= scroll_speed
    for coin in coins:
        coin[0] -= scroll_speed

    if len(obstacles) == 0 or obstacles[-1][0] < WIDTH - 300:
        create_obstacle()
    if len(coins) == 0 or coins[-1][0] < WIDTH - 300:
        create_coin()

    for obstacle in obstacles:
        if player_x + player_width > obstacle[0] and player_x < obstacle[0] + obstacle_width:
            if player_y + player_height > obstacle[1]:
                pygame.quit()
                sys.exit()

    for coin in coins:
        if player_x + player_width > coin[0] and player_x < coin[0] + coin_size:
            if player_y + player_height > coin[1] and player_y < coin[1] + coin_size:
                coins.remove(coin)
                score += 1

    screen.blit(player_img, (player_x, player_y))

    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    for coin in coins:
        pygame.draw.circle(screen, GOLD, (coin[0], coin[1]), coin_size)

    pygame.display.update()

def validate_login():
    global username, password, error_message, is_logged_in
    if username == correct_username and password == correct_password:
        is_logged_in = True
        load_config()  
    else:
        error_message = "Invalid credentials"

def main():
    global username, password, active_input, is_logged_in, input_color
    
    clock = pygame.time.Clock()
    running = True

    while running:
        if not is_logged_in:
            username_rect, password_rect = login_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if username_rect.collidepoint(event.pos):
                        active_input = 'username'
                    elif password_rect.collidepoint(event.pos):
                        active_input = 'password'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        active_input = 'password' if active_input == 'username' else 'username'
                    elif event.key == pygame.K_RETURN:
                        validate_login()
                    elif event.key == pygame.K_BACKSPACE:
                        if active_input == 'username':
                            username = username[:-1]
                        else:
                            password = password[:-1]
                    else:
                        if active_input == 'username':
                            username += event.unicode
                        else:
                            password += event.unicode
        else:
            game_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

        clock.tick(60)

if __name__ == "__main__":
    main()
