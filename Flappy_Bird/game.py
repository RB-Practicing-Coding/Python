import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game settings
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 70
PIPE_HEIGHT = 400
PIPE_GAP = 150
GRAVITY = 1
FLAP_STRENGTH = -10
PIPE_VELOCITY = -4

# Load bird image
bird_img = pygame.image.load("bird.jpg")
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Define Bird class
class Bird:
    def __init__(self):
        self.x = SCREEN_WIDTH // 4
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def flap(self):
        self.velocity = FLAP_STRENGTH

# Define Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = random.randint(PIPE_GAP, SCREEN_HEIGHT - PIPE_GAP)
        self.width = PIPE_WIDTH
        self.height = PIPE_HEIGHT
        self.gap = PIPE_GAP

    def draw(self):
        # Draw top pipe
        pygame.draw.rect(screen, GREEN, (self.x, self.y - self.gap - self.height, self.width, self.height))
        # Draw bottom pipe
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += PIPE_VELOCITY

    def off_screen(self):
        return self.x < -self.width

# Start screen function
def start_pause_screen(mode=0):
    if not mode:
        font = pygame.font.SysFont(None, 55)
        start_img = font.render("Press Space to Start", True, WHITE)
        screen.fill(BLUE)
        screen.blit(start_img, (SCREEN_WIDTH // 2 - start_img.get_width() // 2, SCREEN_HEIGHT // 2 - start_img.get_height() // 2))
        pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

# Main game function
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    start_pause_screen()

    while running:
        screen.fill(BLUE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()
                elif event.key == pygame.K_ESCAPE:
                    start_pause_screen(mode=1)

        # Update bird
        bird.update()

        # Update pipes
        for pipe in pipes:
            pipe.update()
            if pipe.off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe())
                score += 1

        # Collision detection
        for pipe in pipes:
            if bird.x + BIRD_WIDTH > pipe.x and bird.x < pipe.x + pipe.width:
                if bird.y < pipe.y - pipe.gap or bird.y + BIRD_HEIGHT > pipe.y:
                    running = False

        if bird.y > SCREEN_HEIGHT or bird.y < 0:
            running = False

        # Draw everything
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        # Draw score
        font = pygame.font.SysFont(None, 55)
        score_img = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_img, (10, 10))

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
