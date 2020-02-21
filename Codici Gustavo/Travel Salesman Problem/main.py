#!/usr/bin/env python

from __future__ import division, print_function

import cProfile
import random
import sys

import ga
import tsp

if sys.version_info.major == 3:
    from tkinter import *
    xrange = range
else:
    from Tkinter import *


def is_iterable(l):
    try:
        for _ in l:
            return True
        return True
    except TypeError:
        return False


# Tk
def draw_points(root, canvas, l, MIN_COORD, MAX_COORD):
    def drawcircle(canv,x,y,rad):
        return canv.create_oval(x-rad, y-rad, x+rad, y+rad, width=0, fill='red')

    def drawline(canv, x1, y1, x2, y2):
        return canv.create_line(x1, y1, x2, y2, fill='green')

    l = list(l)
    l = l + [l[0]]
    
    BORDA = 10
    
    k_x = (canvas.winfo_width() - 2 * BORDA) / (MAX_COORD - MIN_COORD)
    k_y = (canvas.winfo_height() - 2 * BORDA) / (MAX_COORD - MIN_COORD)
    s_x = BORDA - MIN_COORD * k_x
    s_y = BORDA - MIN_COORD * k_y

    fn_x = lambda n: k_x * n + s_x
    fn_y = lambda n: k_y * n + s_y
    
    canvas.delete(ALL)
    for (x1, y1), (x2, y2) in zip(l[:-1], l[1:]):
        drawline(canvas, fn_x(x1), fn_y(y1), fn_x(x2), fn_y(y2))
    for x1, y1 in l:
        drawcircle(canvas, fn_x(x1), fn_y(y1), 4)

    root.update()


def teste44(sem_nome, tsp_v, MIN_COORD, MAX_COORD, desenhar, root, canvas):
    N = 4
    CROSS_PROB = 0.9
    MUTATION_PROB = 0.9

    ITERATIONS = 4096

    PRINT_PERIOD = 16

    def fn1(m1):
        for i in xrange(ITERATIONS):
            r = ga_v.evolve()
            if i % m1 == 0:
                best = min([(ga_v.obj.calc_distance(j), j) for j in ga_v.chromosomes])
                print(i, best[0], '%i/%i' % (len(set(ga_v.chromosomes)), len(ga_v.chromosomes)))
                if desenhar:
                    p2 = [tsp_v.points[i] for i in best[1]]
                    draw_points(root, canvas, p2, MIN_COORD, MAX_COORD)

    l = []
    if is_iterable(sem_nome):
        for z1 in sem_nome:
            ga_v = teste44(z1, tsp_v, MIN_COORD, MAX_COORD, desenhar, root, canvas)
            l.extend(ga_v.chromosomes)
        ga_v = ga.GA(tsp_v, len(l) // 4, CROSS_PROB, MUTATION_PROB)
        ga_v.set_chromosomes(l)
        fn1(PRINT_PERIOD)
    else:
        ga_v = ga.GA(tsp_v, N, CROSS_PROB, MUTATION_PROB)
        fn1(PRINT_PERIOD)
    return ga_v


def teste5(tsp_v, MIN_COORD=None, MAX_COORD=None):
    desenhar = MIN_COORD is not None and MAX_COORD is not None
    if desenhar:
        root = Tk()

        canvas = Canvas(width=450, height=450, bg='black')
        canvas.pack(expand=YES, fill=BOTH)
        root.update()
    else:
        root = canvas = None

    return teste44([[[[None, None], [None, None]], [[None, None], [None, None]]], [[[None, None], [None, None]], [[None, None], [None, None]]]], tsp_v, MIN_COORD, MAX_COORD, desenhar, root, canvas)


def teste1(num_points):
    MIN_COORD = 0
    MAX_COORD = 100
    
    points = [(random.randrange(0, MAX_COORD), random.randrange(0, 100)) for _ in xrange(num_points)]

    tsp_v = tsp.TSP(points)

    ga_v = teste5(tsp_v, MIN_COORD, MAX_COORD)
    bests = sorted([(ga_v.obj.calc_distance(j), j) for j in ga_v.chromosomes])
    for i in xrange(10):
        print(bests[i][0])
    return ga_v


if __name__ == '__main__':
    ga_v = teste1(100)
