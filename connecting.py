import pygame
import sys
import random
import tetrismini

# set up display
screen = pygame.display.set_mode([1000, 750])

# load the icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("The Bio-Informatic")

pygame.init()

# load the background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (1000, 1000))

# Get the dimensions of the screen and the background image
screen_width, screen_height = screen.get_size()
background_width, background_height = background.get_size()

# Calculate the top-left coordinates to center the background
background_x = (screen_width - background_width) // 2
background_y = (screen_height - background_height) // 2

#load the website bc it doenst work otherwise omg
website = pygame.image.load("website.png")
website = pygame.transform.scale(website, (1000,800))
website_rect = website.get_rect()
website_y = (screen_height - website_rect.height) // 2
website_x = 0
website_y += 20
website_rect.topleft = [website_x, website_y]

# Load the obstacle image
obstacle = pygame.image.load("obstacle.png")
obstacle = pygame.transform.scale(obstacle, (400, 400))
obstacle_rect = obstacle.get_rect()
# Position of the obstacle
obstacle_y = (screen_height - obstacle_rect.height) // 2
obstacle_x = 800  # Adjust this value to move the obstacle more to the left
obstacle_y += 240
# Set the position of the obstacle
obstacle_rect.topleft = [obstacle_x, obstacle_y]

# Load "hint" poster image
poster = pygame.image.load("poster.png")
poster = pygame.transform.scale(poster, (200, 200))
poster_rect = poster.get_rect()
poster_y = (screen_height - poster_rect.height) // 2
poster_x = 820
poster_y += -220
poster_rect.topleft = [poster_x, poster_y]

# Load the virus icon image
virus = pygame.image.load("virus.png")
virus = pygame.transform.scale(virus, (50, 50))
virus_rect = virus.get_rect()
# Position of the virus icon
virus_y = (screen_height - virus_rect.height) // 2
virus_x = 230
virus_y += -220
virus_rect.topleft = [virus_x, virus_y]

tetrisvirus = pygame.image.load("tetrisvirus.png")
tetrisvirus = pygame.transform.scale(tetrisvirus, (50, 50))
tetrisvirus_rect = tetrisvirus.get_rect()

tetrisvirus_y = (screen_height - tetrisvirus_rect.height) // 2
tetrisvirus_x = 280
tetrisvirus_y += -180
tetrisvirus_rect.topleft = [tetrisvirus_x, tetrisvirus_y]



# load the player
player = pygame.image.load("player.png")
# sets how big the player is
player_width = 75
player_height = 75
player = pygame.transform.scale(player, (player_width, player_height))
player_rect = player.get_rect()
player_rect.topleft = [500, 375]  # Initial position at the center of the screen

# load the dna


# movement speed
speed = 6

font = pygame.font.Font(None, 36)

def coordinatemaker(num_coords):
    """Generates a list of unique random coordinates as tuples.
    :param num_coords: amount of coordinates to generate.
    : return coords: the coordinates
    """
    coords = []
    while len(coords) < num_coords:
        new_coord = (random.randint(50, 750), random.randint(100, 500))
        if new_coord not in coords:
            coords.append(new_coord)
    return coords

# Password function
def check_password():
    """
    This function checks if the password is correct.
    :return user_text: The user input text
    """
    input_active = True
    user_text = ""  # The user types the password in this string
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    return user_text
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        # Draw everything
        # blit copies an area from one surface to another
        screen.blit(background, (background_x, background_y))
        screen.blit(obstacle, obstacle_rect)
        screen.blit(virus, virus_rect)
        screen.blit(player, player_rect)

        # Render "Enter password" text
        prompt_surface = font.render("Please enter the password:", True, (174, 29, 123))
        screen.blit(prompt_surface, (screen_width // 2 - 170, screen_height // 2 - 60))

        # Render the current text
        text_surface = font.render(user_text, True, (174, 29, 123))
        screen.blit(text_surface, (screen_width // 2 - 75, screen_height // 2 - 20))

        pygame.display.flip()

    return user_text


def display_message(message, color, x, y):
    """
    This function renders the given message and displays it on the screen for 2 seconds.
    :param message: The message to be displayed
    :param color: RGB color picker
    :param x: horizontal
    :param y: vertical
    """
    # .render is a module to render and loading in a font (message, color)
    message_surface = font.render(message, True,color)
    screen.blit(message_surface, (x, y))
    pygame.display.flip()
    pygame.time.delay(2000)  # Display the message for 2 seconds

def display_img(img_img, img_size, img_horizontal, img_vertical):
    """
    This function renders the given image and displays it on the screen for 2 seconds.
    :param img_img: the file of the image
    :param img_size: the size of the image
    :param img_horizontal: the horizontal position
    :param img_vertical: the vertical position

    """
    img_surface = pygame.image.load(img_img)
    img_surface = pygame.transform.scale(img_surface,img_size)
    img_surface_rect = img_surface.get_rect()
    img_y = (screen_height - img_surface_rect.height) // 2
    img_x = img_horizontal
    img_y += img_vertical
    img_surface_rect.topleft = [img_x, img_y]
    screen.blit(img_surface, img_surface_rect)
    pygame.display.flip()
    pygame.time.delay(1000)


def mini_game():
    """
    This function is a mini game for in the main game, ai wrote this code for me and i added some aspects myself, like the pairs
    ( the amount of pairs, this was a pain in the ass).
    :return:
    """
    # Define colors
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (210, 1, 3)
    pink = (255, 195, 252)

    # Generate positions for 12 items (6 pairs)
    positions = coordinatemaker(12)

    # Randomly assign positions to the pairs
    random.shuffle(positions)
    pairs = [(positions[i], positions[i + 1]) for i in range(0, 12, 2)]

    # Load images
    alanine_img = pygame.image.load('alanine.png')
    thymine_img = pygame.image.load('thymine.png')
    cytosine_img = pygame.image.load('cytosine.png')
    guanine_img = pygame.image.load('guanine.png')

    # Create rectangles for each pair
    alanine_rects = [alanine_img.get_rect(topleft=pos[0]) for pos in pairs[:3]]
    thymine_rects = [thymine_img.get_rect(topleft=pos[1]) for pos in pairs[:3]]
    cytosine_rects = [cytosine_img.get_rect(topleft=pos[0]) for pos in pairs[3:]]
    guanine_rects = [guanine_img.get_rect(topleft=pos[1]) for pos in pairs[3:]]

    # Circle sets and their rectangles
    circle_sets = [
        [(alanine_rects[i], alanine_img) for i in range(3)] + [(thymine_rects[i], thymine_img) for i in range(3)],
        [(cytosine_rects[i], cytosine_img) for i in range(3)] + [(guanine_rects[i], guanine_img) for i in range(3)]
    ]

    # Variables to track clicks and lines
    clicked_positions = []
    lines = []

    # Function to check if the connection is correct within a set
    def is_correct_connection(start_pos, end_pos):
        start_rect = next((rect for rect, img in circle_sets[0] if rect.center == start_pos), None)
        end_rect = next((rect for rect, img in circle_sets[0] if rect.center == end_pos), None)
        if start_rect and end_rect:
            return (start_rect in alanine_rects and end_rect in thymine_rects) or (
                        start_rect in thymine_rects and end_rect in alanine_rects)

        start_rect = next((rect for rect, img in circle_sets[1] if rect.center == start_pos), None)
        end_rect = next((rect for rect, img in circle_sets[1] if rect.center == end_pos), None)
        if start_rect and end_rect:
            return (start_rect in cytosine_rects and end_rect in guanine_rects) or (
                        start_rect in guanine_rects and end_rect in cytosine_rects)

        return False

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
                    else:
                        lines.append((clicked_positions[0], clicked_positions[1], red))
                        display_message("Wrong connection!", (255, 38, 178), screen_width // 2 - 75,
                                        screen_height // 2 + 20)
                    clicked_positions = []

                    # Check if all correct connections are made
                    if len(lines) == 6:
                        display_img("dna.png", (700, 700), 150, 10)
                        display_img("dna_reverse.png", (700, 700), 150, 10)
                        display_img("dna.png", (700, 700), 150, 10)
                        display_img("dna_reverse.png", (700, 700), 150, 10)
                        display_message("All correct connections are made! You did great!", (255, 38, 178),
                                        screen_width // 2 - 285, screen_height // 2 + 300)
                        rungame()

                        running = False

        # Fill the screen the image
        screen.blit(website, website_rect)

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



def rungame():

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and player_rect.colliderect(virus_rect):
                    password = check_password()
                    # sets password: Depression
                    if password == "Depression":
                        display_message("Access granted!", (255, 38, 178), screen_width // 2 - 75,
                                        screen_height // 2 + 20)
                        mini_game()
                    else:
                        display_message("Access denied!", (228, 8, 10), screen_width // 2 - 75, screen_height // 2 + 20)
                elif event.button == 1 and player_rect.colliderect(tetrisvirus_rect):
                    print("test")
                    password = check_password()
                    if password == "silly":
                        display_message("Access granted!", (255, 38, 178), screen_width // 2 - 75,
                                        screen_height // 2 + 20)
                        tetrismini.main()

                    else:
                        display_message("Access denied!", (228, 8, 10), screen_width // 2 - 75, screen_height // 2 + 20)



        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_rect.x -= speed
            # undo movement if the player is near obstacle
            if player_rect.colliderect(obstacle_rect) or player_rect.left < 0:
                player_rect.x += speed
        if keys[pygame.K_d]:
            player_rect.x += speed
            if player_rect.colliderect(obstacle_rect) or player_rect.right > screen_width:
                player_rect.x -= speed
        if keys[pygame.K_w]:
            player_rect.y -= speed
            if player_rect.colliderect(obstacle_rect) or player_rect.top < 0:
                player_rect.y += speed
        if keys[pygame.K_s]:
            player_rect.y += speed
            if player_rect.colliderect(obstacle_rect) or player_rect.bottom > screen_height:
                player_rect.y -= speed

        # Draw the background
        screen.blit(background, (background_x, background_y))

        # Draw the obstacle
        screen.blit(obstacle, obstacle_rect)
        screen.blit(virus, virus_rect)
        screen.blit(tetrisvirus, tetrisvirus_rect)
        screen.blit(poster, poster_rect)


        # Draw player
        screen.blit(player, player_rect)
        pygame.display.update()

if __name__ == "__main__":
    print("running connecting.py")
    rungame()
    print("Run complete")