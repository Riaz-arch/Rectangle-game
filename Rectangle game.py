import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangular Sprites Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the rectangle class
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# Create two rectangles
rect1 = Rectangle(100, 100, 50, 50, RED)  # Player-controlled rectangle
rect2 = Rectangle(300, 300, 50, 50, BLUE)  # Static rectangle

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Control the first rectangle with arrow keys
    if keys[pygame.K_LEFT]:
        rect1.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        rect1.move(5, 0)
    if keys[pygame.K_UP]:
        rect1.move(0, -5)
    if keys[pygame.K_DOWN]:
        rect1.move(0, 5)

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the rectangles
    rect1.draw(screen)
    rect2.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)