import pygame


pygame.init()

running = True

intro = pygame.image.load("1.png")

screen = pygame.display.set_mode(
    (intro.get_width()*0.5, intro.get_height()*0.5))

intro = pygame.transform.scale(
    intro, (screen.get_width(), screen.get_height()))
# screen = pygame.display.set_mode(
#     (300, 300))
screen.blit(intro, (0, 0))

pygame.display.flip()

size = None


def askDisplay():
    question1_font = pygame.font.Font(None, 30)
    question1 = question1_font.render(
        "Enter board size, 3, 4, 5: ", True, (0, 0, 0))


def display():
    board = [['' for _ in range(size)] for _ in range(size)]
    print(board)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            display()


# two modes, multiplayer and single player
# if multiplayer:
# enter number of rounds
# split screen into columns, middle has board, board will be an image so it does not need a class,
# game will alternate between the two, both have different symbols and should be able to place them after each other
# score updates on the side

# for single player
# screen again splits
# ask for number of rounds
# opponent will be the computer playing, place the symbol in random places on the board, within the spots (this may be challenging)
# score gets tallied on the side

# when game is over
# winner symbol is displayed, asked to play again or quit

pygame.quit()
