import pygame.draw
import random
from Constants import *

class Spot:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.h = 0
        self.g = 0
        self.f = 0
        self.neighbors = []
        self.prev = 0
        self.wall = False

        if random.random() < 0.2:
            self.wall = True

    def draw(self, win, color, stroke):
        pygame.draw.rect(win, color, (self.i * W, self.j * H, W, H), stroke)

    def add_neighbor(self, grid):
        i = self.i
        j = self.j

        if i < COLUMN - 1:
            self.neighbors.append(grid[i+1][j])
        if i > 0:
            self.neighbors.append(grid[i-1][j])
        if j < ROW - 1:
            self.neighbors.append(grid[i][j+1])
        if j > 0:
            self.neighbors.append(grid[i][j-1])
