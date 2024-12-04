import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Connect the Dots")

# Define colors
black = (0, 0, 0)
green = (0, 255, 0)
purple = (128, 0, 128)
white = (255, 255, 255)

# Possible positions
positions = [(50, 100), (150, 200), (250, 300), (350, 400), (450, 500), (550, 100), (650, 200), (750, 300), (150, 400), (250, 500)]

# Randomly assign positions to the pairs
alanine_pos = random.choice(positions)
positions.remove(alanine_pos)
thymine_pos = random.choice(positions)
positions.remove(thymine_pos)

cytosine_pos = random.choice(positions)
positions.remove(cytosine_pos)
guanine_pos = random.choice(positions)
positions.remove(guanine_pos)

# Load images
alanine_img = pygame.image.load('alanine.png')
thymine_img = pygame.image.load('thymine.png')
cytosine_img = pygame.image.load('cytosine.png')
guanine_img = pygame.image.load('guanine.png')

# Get image rectangles
alanine_rect = alanine_img.get_rect(topleft=alanine_pos)
thymine_rect = thymine_img.get_rect(topleft=thymine_pos)
cytosine_rect = cytosine_img.get_rect(topleft=cytosine_pos)
guanine_rect = guanine_img.get_rect(topleft=guanine_pos)

# Circle sets and their rectangles
circle_sets = [
    [(alanine_rect, alanine_img), (thymine_rect, thymine_img)],  # Set 1
    [(cytosine_rect, cytosine_img), (guanine_rect, guanine_img)]  # Set 2
]

# Define correct connections
correct_connections = [
    (alanine_rect.center, thymine_rect.center),
    (cytosine_rect.center, guanine_rect.center)
]

# Variables to track clicks and lines
clicked_positions = []
lines = []

# Function to check if the connection is correct within a set
def is_correct_connection(start_pos, end_pos):
    return (start_pos, end_pos) in correct_connections or (end_pos, start_pos) in correct_connections

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for circle_set in circle_sets:
                for rect, img in circle_set:
                    if rect.collidepoint(mouse_pos):
                        clicked_positions.append(rect.center)
                        break
            # If two images are clicked, check the connection
            if len(clicked_positions) == 2:
                if is_correct_connection(clicked_positions[0], clicked_positions[1]):
                    lines.append((clicked_positions[0], clicked_positions[1], green))
                    print("Correct connection!")
                else:
                    lines.append((clicked_positions[0], clicked_positions[1], purple))
                    print("Wrong connection!")
                clicked_positions = []

                # Check if all correct connections are made
                if all(conn in [(line[0], line[1]) for line in lines] or (conn[1], conn[0]) in [(line[0], line[1]) for line in lines] for conn in correct_connections):
                    print("All correct connections made! Game Over!")
                    running = False

    # Fill the screen with white
    screen.fill(white)

    # Draw images
    for circle_set in circle_sets:
        for rect, img in circle_set:
            screen.blit(img, rect.topleft)

    # Draw all lines
    for line in lines:
        pygame.draw.line(screen, line[2], line[0], line[1], 5)

    # Redraw the line if it has been drawn
    if len(clicked_positions) == 1:
        pygame.draw.line(screen, black, clicked_positions[0], pygame.mouse.get_pos(), 5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()