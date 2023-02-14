'''snake game by Polstyanov Ivan
ver.0.4.'''
import pygame as pg
import random
import grid

framex, framey = 480, 480
frameY = framey + 240
pg.init()
pg.display.set_caption('Snake Game better tame')
game_window = pg.display.set_mode((framex, frameY))

black = pg.Color(33, 33, 33)
white = pg.Color(202, 202, 202)
red = pg.Color(188, 44, 44)
green = pg.Color(44, 188, 44)
gray = pg.Color(166, 166, 166)
snake = [240, 430]
snbody = [[50, 100], [50, 90], [50, 80], [50, 70]]
food = [random.randrange(1, (framex // 10)) * 10,
        random.randrange(1, (framey // 10)) * 10]
bounds, vector, difficulty, diffactor, score, pause = True, 'UP', 10, 10, 0, False
grid = grid.Grid(surface=game_window, cellSize=10, color=gray)


def game_over():
    game_window.fill(white)
    onscreen(framex / 2, frameY / 2, 'times new roman', 70, 'THE END')
    onscreen(framex / 2, frameY / 4, 'consolas', 20, f"Score: {score}        Difficulty: {difficulty}")
    pg.display.flip()
    pg.time.wait(5000)
    pg.quit()


def gameovercondition(bs):
    if bs:
        if snake[0] < 0: snake[0] = framex - 10
        if snake[0] > framex - 10: snake[0] = -10
        if snake[1] < 0: snake[1] = framey - 10
        if snake[1] > framey - 10: snake[1] = -10
    else:
        if snake[0] < 0 or snake[0] > framex - 10: game_over()
        if snake[1] < 0 or snake[1] > framey - 10: game_over()
    for block in snbody[1:]:
        if snake[0] == block[0] and snake[1] == block[1]: game_over()


def onscreen(x, y, font, size, text):
    ofont = pg.font.SysFont(font, size)
    osurface = ofont.render(text, True, black)
    orect = osurface.get_rect()
    orect.midbottom = (x, y)
    game_window.blit(osurface, orect)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_UP:
                    vector = 'UP' if vector != 'DOWN' else 'DOWN'
                case pg.K_DOWN:
                    vector = 'DOWN' if vector != 'UP' else 'UP'
                case pg.K_LEFT:
                    vector = 'LEFT' if vector != 'RIGHT' else 'RIGHT'
                case pg.K_RIGHT:
                    vector = 'RIGHT' if vector != 'LEFT' else 'LEFT'
                case 61:
                    diffactor += 1
                case pg.K_MINUS:
                    diffactor -= 1
                case 98:
                    bounds = not bounds
                case 112:
                    pause, difficulty = difficulty, pause
                case pg.K_ESCAPE:
                    pg.event.post(pg.event.Event(pg.QUIT))
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = event.pos
            # cells[pos[1]//10][pos[0]//10] = 1
    if not difficulty:
        continue
    match vector:
        case 'UP':
            snake[1] -= 10
        case 'DOWN':
            snake[1] += 10
        case 'LEFT':
            snake[0] -= 10
        case 'RIGHT':
            snake[0] += 10

    gameovercondition(bounds)

    snbody.insert(0, list(snake))
    if snake[0] == food[0] and snake[1] == food[1]:
        score += 1
        food = [random.randrange(1, (framex // 10)) * 10,
                random.randrange(1, (framey // 10)) * 10]
    else:
        snbody.pop()

    game_window.fill(white)
    grid.drawUseLine()
    for pos in snbody:
        pg.draw.rect(game_window, green, pg.Rect(pos[0], pos[1], 10, 10))
    pg.draw.rect(game_window, red, pg.Rect(food[0], food[1], 10, 10))
    pg.draw.rect(game_window, gray, pg.Rect(0, framex, framey, frameY))
    onscreen(framex / 2, frameY - 25, 'consolas', 20, f"Score: {score}          Difficulty: {difficulty}")
    onscreen(framex / 2, frameY - 50, 'consolas', 20, f"Bounds: {'OFF' if bounds else 'ON':3}                     ")
    onscreen(framex / 2, frameY - 190, 'consolas', 18, "'P' turn Pause           'B' to toggle bounds")
    onscreen(framex / 2, frameY - 165, 'consolas', 18, "'+/-' change Difficulty        Arrows to move")
    difficulty = abs(diffactor) + score // 5
    pg.time.Clock().tick(difficulty)
    pg.display.update()
