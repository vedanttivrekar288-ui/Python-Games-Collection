import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25, bold=True)

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GRAY = (55, 55, 55)
GREEN = (35, 120, 50)
BLUE = (30, 120, 255)
RED = (230, 50, 50)

car_width = 50
car_height = 90

def reset_game():
    return (
        pygame.Rect(225, 580, car_width, car_height),
        pygame.Rect(random.randint(85, 365), -100,
                    car_width, car_height),
        0, 5, False
    )

player, enemy, score, speed, game_over = reset_game()
road_offset = 0

def draw_car(car, color):
    pygame.draw.rect(screen, BLACK,
                     (car.x - 5, car.y + 12, 10, 20))
    pygame.draw.rect(screen, BLACK,
                     (car.right - 5, car.y + 12, 10, 20))
    pygame.draw.rect(screen, BLACK,
                     (car.x - 5, car.y + 60, 10, 20))
    pygame.draw.rect(screen, BLACK,
                     (car.right - 5, car.y + 60, 10, 20))

    pygame.draw.rect(screen, color, car, border_radius=10)

    pygame.draw.rect(screen, (170, 210, 230),
                     (car.x + 7, car.y + 18, 36, 20),
                     border_radius=4)

    pygame.draw.rect(screen, BLACK,
                     (car.x + 7, car.y + 60, 36, 15),
                     border_radius=4)

    pygame.draw.rect(screen, WHITE,
                     (car.x + 5, car.y + 3, 12, 6))
    pygame.draw.rect(screen, WHITE,
                     (car.right - 17, car.y + 3, 12, 6))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player, enemy, score, speed, game_over = reset_game()

            if event.key == pygame.K_ESCAPE:
                running = False

    if not game_over:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= 7

        if keys[pygame.K_RIGHT]:
            player.x += 7

        player.x = max(85, min(player.x, 365))

        enemy.y += speed
        road_offset = (road_offset + speed) % 100

        if enemy.top > HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(85, 365)
            score += 10
            speed += 0.5

        if player.colliderect(enemy):
            game_over = True

    screen.fill(GREEN)

    pygame.draw.rect(screen, GRAY, (70, 0, 360, HEIGHT))

    pygame.draw.line(screen, WHITE,
                     (75, 0), (75, HEIGHT), 5)
    pygame.draw.line(screen, WHITE,
                     (425, 0), (425, HEIGHT), 5)

    for y in range(-100, HEIGHT, 100):
        pygame.draw.rect(screen, WHITE,
                         (247, y + road_offset, 6, 50))

    draw_car(player, BLUE)
    draw_car(enemy, RED)

    score_text = font.render(
        f"Score: {score}", True, WHITE
    )
    screen.blit(score_text, (15, 15))

    if game_over:
        pygame.draw.rect(screen, BLACK,
                         (40, 250, 420, 170),
                         border_radius=15)

        text = font.render("GAME OVER", True, RED)
        screen.blit(text, text.get_rect(center=(250, 285)))

        text = font.render(
            f"Final Score: {score}", True, WHITE
        )
        screen.blit(text, text.get_rect(center=(250, 330)))

        text = font.render(
            "Press R to Restart", True, WHITE
        )
        screen.blit(text, text.get_rect(center=(250, 375)))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
