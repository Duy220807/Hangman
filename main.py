import pygame
import random

pygame.init()

# Kích thước màn hình
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")

# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Cấu hình trò chơi
font = pygame.font.SysFont(None, 55)
word_list = ["PYTHON", "HANGMAN", "PYTHONIC", "DEVELOPER"]
word = random.choice(word_list)
guessed_letters = []
attempts = 6

def draw():
    win.fill(black)
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    text = font.render(display_word, True, white)
    win.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.update()

def main():
    global attempts
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                letter = pygame.key.name(event.key).upper()
                if letter in word and letter not in guessed_letters:
                    guessed_letters.append(letter)
                elif letter not in word:
                    attempts -= 1
                    if attempts <= 0:
                        print("Game Over! The word was:", word)
                        run = False

        draw()
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word.")
            run = False

    pygame.quit()

if __name__ == "__main__":
    main()
