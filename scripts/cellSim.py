#!/usr/bin/env python3
import pygame
import sys
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
width = 25
height = 25
margin = 1
wind0w = [260, 260]

class livingCell:
    def __init__(self):
        pass


class deadCell:
    def __init__(self):
        pass


class multiCell:

    def __init__(self):
        pass


def cellStart():

    # Create random cords
    grid = []
    for row in range(10):
        grid.append([randint(0, 10)*5])
        for column in range(10):
            grid[row].append(randint(0, 10))


    # n = input('how many Cells to Start with? : ')
    pygame.init()
    clock = pygame.time.Clock()  # adjust how fast screen updates
    screen = pygame.display.set_mode(wind0w)
    pygame.display.set_caption("cellSim")
    font = pygame.font.Font(None, 30)
    text = font.render("Click to begin", True, white)
    screen.blit(text, (60, 100))
    pygame.display.update()
    done = False  # loop until close

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # exit loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #### random cells on mouse click
                pos = pygame.mouse.get_pos()
                # THIS APPARENTLY CHANGES X/Y SCREEN COORDS TO GRID COORDS
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                # color cell on click
                grid[row][column] = 1
                # show current X, Y coordinates
                print(pos, "box coords: ", row, column)
                screen.fill(black)
                pygame.display.update()
                # Draw Grid
                for row in range(10):
                    for column in range(10):
                        if grid[row][column] == 1:
                            color = green
                            pygame.draw.rect(screen,
                                             color,
                                             [(margin + width) * column + margin,
                                              (margin + height) * row + margin,
                                              width,
                                              height])
                            pygame.display.update()
                        elif grid[row][column] != 1 :
                            color = red
                            pygame.draw.rect(screen,
                                             color,
                                             [(margin + width) * column + margin,
                                              (margin + height) * row + margin,
                                              width,
                                              height])
                            color = red
                            pygame.display.update()
                        else:
                            pygame.quit()
                            sys.exit()


cellStart()
