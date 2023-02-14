import pygame

GRID_COORD_MARGIN_SIZE = 0


class Grid():
    def __init__(self, surface, cellSize, color):
        self.surface = surface
        self.colNb = surface.get_width() // cellSize
        self.lineNb = surface.get_height() // cellSize
        self.cellSize = cellSize
        self.grid = [[0 for i in range(self.colNb)] for j in range(self.lineNb)]
        self.color = color

    def drawUseLine(self):
        for li in range(self.lineNb):
            liCoord = GRID_COORD_MARGIN_SIZE + li * self.cellSize
            pygame.draw.line(self.surface, self.color, (GRID_COORD_MARGIN_SIZE, liCoord),
                             (self.surface.get_width(), liCoord))
        for co in range(self.colNb):
            colCoord = GRID_COORD_MARGIN_SIZE + co * self.cellSize
            pygame.draw.line(self.surface, self.color, (colCoord, GRID_COORD_MARGIN_SIZE),
                             (colCoord, self.surface.get_height()))
