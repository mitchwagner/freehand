from collections import namedtuple

Point = namedtuple('Point', 'x y')


def draw_point(point, color, canvas):
    print(point)
    canvas[point.x][point.y] = color

    return canvas


def draw_line(top_left, bottom_right, color, canvas):
    # TODO: get a list of points
    points = [Point(0, 0), Point(1, 1), Point(2, 2)]
    fs = [curried_draw_point(p) for p in points] 
    
    return compose(fs, canvas)


def curried_draw_point(point, color=(0, 0, 0)):
    print(point)
    return lambda canvas: draw_point(point, color, canvas)


def curried_draw_line(top_left, bottom_right, color):
    return lambda canvas: draw_line(top_left, bottom_right, color, canvas)


def compose(fs, c):
    return compose(fs[1:], fs[0](c)) if fs else c
