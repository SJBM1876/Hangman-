import pygame
import math
import random


# Display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")

# Buttons
RADIUS = 25
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 30 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Font
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 80)

# Image
screen = pygame.display.set_mode((1500, 600))
image = pygame.image.load("hangman0.jpg")

images = []
for i in range(11):
    image = pygame.image.load("hangman" + str(i) + ".jpg")
    images.append(image)

# Game
hangman_status = 0
word_list = ["APPLE", "BANANA", "CARROT", "DOG", "ELEPHANT",
    "FLOWER", "GUITAR", "HOUSE", "ISLAND", "JUNGLE",
    "KITE", "LION", "MOUNTAIN", "NOTEBOOK", "OCEAN",
    "PENGUIN", "QUEEN", "RIVER", "SUN", "TREE",
    "UMBRELLA", "VOLCANO", "WATERFALL", "XYLOPHONE", "YACHT",
    "ZEBRA", "BEACH", "CANDLE", "DOLPHIN", "EAGLE",
    "FOREST", "GIRAFFE", "HELICOPTER", "ICECREAM", "JACKET",
    "KANGAROO", "LIGHTHOUSE", "MANGO", "NIGHT", "OCTOPUS",
    "PIANO", "QUOKKA", "RAINBOW", "SUNSET", "TIGER",
    "UNICORN", "VIOLIN", "WATERMELON", "XYLOPHONE", "YAK",
    "ZEPPELIN"]
word = random.choice(word_list)
guessed = []

# Colour
SKYBLUE = (135, 206, 235)
WHITE = (255, 255, 255)

def draw():
    win.fill(SKYBLUE)

    # Title
    text = TITLE_FONT.render("HANGMAN", 1, WHITE)
    win.blit(text, (WIDTH/1.2 - text.get_width()/2, 20))

    # Game word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, WHITE)
    win.blit(text, (550, 200))

    # Buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, WHITE, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, WHITE)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(SKYBLUE)
    text = WORD_FONT.render(message, 1, WHITE)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
      clock.tick(FPS)


      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
      draw()

      won = True
      for letter in word:
          if letter not in guessed:
              won = False
              break
        
      if won:
          display_message("You WON!")
          break

      if hangman_status == 10:
          display_message("You LOST!")
          break


def display_message(message):
    pygame.time.delay(1000)
    win.fill(SKYBLUE)
    text1 = WORD_FONT.render(message, 1, WHITE)
    text2 = WORD_FONT.render(f"The word was: {word}", 1, WHITE)
    win.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT/2 - 50))
    win.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2 + 50))
    pygame.display.update()
    pygame.time.delay(3000)

while True:
    # Reset the game state
    word = random.choice(word_list)
    guessed = []
    hangman_status = 0

    # Reset the button states
    for letter in letters:
        letter[3] = True

    main()
    
pygame.quit()
