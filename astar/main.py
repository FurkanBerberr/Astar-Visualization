import pygame
from Constants import *
from Spot import *
import math

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astar")


openSet = []
closeSet = []
grid = [[Spot(j, i) for i in range(COLUMN)] for j in range(ROW)]
[[grid[i][j].add_neighbor(grid) for i in range(COLUMN)] for j in range(ROW)]
# Start node
start = grid[0][0]
start.wall = False
# End node
end = grid[COLUMN - 1][ROW - 1]
end.wall = False
# Adding the start node to open set
openSet.append(start)
path = []

def draw_window(win):
    win.fill((255, 255, 255))
    for i in grid:
        for j in i:
            if not j.wall:
                j.draw(win, (0, 0, 0), 1)
            else:
                j.draw(win, (0, 0, 0), 0)

    for i in openSet:
        i.draw(win, GREEN, 0)

    for i in closeSet:
        i.draw(win, RED, 0)

    for i in path:
        i.draw(win, (0, 0, 255), 0)

    pygame.display.update()


def heuristic(start, finish):
    # p1 = [start.i, start.j]
    # p2 = [finish.i, finish.j]
    # distance = math.dist(p1, p2)
    # return distance

    d = abs(start.i - finish.i) + abs(start.j - finish.j)
    return d

def astar_loop():
    if len(openSet) > 0:
        winner = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[winner].f:
                winner = i

        current = openSet[winner]
        if current == end:
            temp = current
            path.append(temp)
            while temp.prev:
                path.append(temp.prev)
                temp = temp.prev
            return

        openSet.remove(current)
        closeSet.append(current)

        neighbors = current.neighbors
        for neighbor in neighbors:
            if neighbor not in closeSet and not neighbor.wall:
                tempG = neighbor.g + 1
                if neighbor in openSet:
                    if tempG < neighbor.g:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openSet.append(neighbor)

                neighbor.h = heuristic(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.prev = current



def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        astar_loop()
        draw_window(win)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()