"""
My custom module for TicTacToe.
Author: Shashank
Date: July 10, 2024
"""
import pygame as py


def Dimb12(a, Dim):
    return (Dim*a)/12

def make_rectangles(Dim : int, row, col):
    arr = []
    Db12 = Dimb12(1,Dim)
    recw, rech = (10/col) * Db12, (10/row) * Db12

    for i in range(col):
        temp = []
        for j in range(row):
            recx, recy = (1 + j * (recw/Db12))* Db12, (1 + i * (rech/Db12))* Db12
            temp.append(py.Rect(recx,recy, recw, rech))
        arr.append(temp)

    return arr



def init_screen(ROW, COL, screen, rects):
    screen.fill((255, 255, 255))
# Draw the grid lines
    for i in range(1, ROW):
        py.draw.line(screen, "black", (rects[0][i][0], rects[0][i][1]),(rects[ROW -1][i][0], rects[ROW - 1][i][1] + rects[0][0][3]), 1)
    for j in range(1, COL):
        py.draw.line(screen, "black", (rects[j][0][0], rects[j][0][1]),(rects[j][COL- 1][0] + rects[0][0][2], rects[j][COL - 1][1]), 1)


def call_win(WINDOW_SIZE, screen, base_font, Playerchar):
        winstr ="Beteee! Mauj Karadi !"
        print(winstr)
        text_screen = base_font.render(Playerchar + " Won !", True, (14,200,200))
        screen.blit(text_screen, (WINDOW_SIZE * 0.1, WINDOW_SIZE * 0.02))


         