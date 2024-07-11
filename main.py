import pygame as pg
import sys
import header as h
import grid as g

pg.init()

WINDOW_SIZE = 500
ROW, COL = 3,3 # can be customized but 1 or 2 feature might not work properly
MARGIN = WINDOW_SIZE / 12
RECW = (10/COL) * MARGIN
RECH = (10/ROW) * MARGIN
TEXTSIZE = int(min(RECW, RECH) * 0.6)
GO = True # Game On


screen = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
base_font = pg.font.Font(None, TEXTSIZE)
pg.display.set_caption('Tic Tac Toe')
clock = pg.time.Clock()
rects = h.make_rectangles(WINDOW_SIZE, ROW, COL)
rect_color = (255, 0, 0)


clickerxy= []
grid = []
PlayerChar = "X"


h.init_screen(ROW, COL, screen, rects)

# Init cirtual rects
for rect in rects:
    for r in rect:
        pg.draw.rect(screen, rect_color, r, -1)


PlayerChar = "X"    
PlayerHistory = []

# Main game loop
# Grid can be of m x n where m and both can be any natural number
grid = g.make_grid(ROW, COL)

while GO:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # Check if mouse click collides with the rectangle             
            mouse_pos = pg.mouse.get_pos()
            for i in range(ROW):
                for j in range(COL):
                    if rects[i][j].collidepoint(mouse_pos):
                        print("Rectangle clicked!")
                        if grid[i][j] == "0":
                            text_screen = base_font.render(PlayerChar, True, (0,0,0))
                            textX = MARGIN + RECW * j + RECW / 2 - TEXTSIZE/4
                            textY = MARGIN + RECH * i + RECH / 2 - TEXTSIZE/4
                            screen.blit(text_screen, (textX, textY))
                            pg.display.flip()
                            
                            grid[i][j] = PlayerChar
                            
                            print(grid)
                            
                            win = g.check_win(grid, PlayerChar)
                            
                            if win == 1:
                                GO= False
                                base_font2 = pg.font.Font(None, 32)
                                h.-call_win(WINDOW_SIZE, screen, base_font2, PlayerChar)
                                break
                            
                            PlayerHistory.append([i,j])
                            if len(PlayerHistory) == ROW * COL:

                                """
                                text_screen = base_font.render("", True, (0,0,0))
                                textX = MARGIN + RECW * PlayerHistory[0][1] + RECW / 2 - TEXTSIZE/4
                                textY = MARGIN + RECH * PlayerHistory[0][0] + RECH / 2 - TEXTSIZE/4
                                screen.blit(text_screen, (textX, textY))
                                """
                                grid[PlayerHistory[0][0]][PlayerHistory[0][1]] = "0"
                                print(grid)    
                                PlayerHistory[0: ROW * COL - 1] = PlayerHistory[1: ROW * COL]
                                PlayerHistory.pop()
                                h.init_screen(ROW, COL, screen, rects)
                                for i in range(len(grid)):
                                    for j in range(len(grid[i])):
                                        if grid[i][j] != '0':
                                            text_screen = base_font.render(grid[i][j], True, (0,0,0))
                                            textX = MARGIN + RECW * j + RECW / 2 - TEXTSIZE/4
                                            textY = MARGIN + RECH * i + RECH / 2 - TEXTSIZE/4
                                            screen.blit(text_screen, (textX, textY))
                                                
                            if PlayerChar == 'O':
                                PlayerChar = 'X'
                            elif PlayerChar == 'X':
                                PlayerChar = 'O'
                                                
                             
    pg.display.flip()
    clock.tick(60)

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()