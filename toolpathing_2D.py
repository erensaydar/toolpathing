from data_structures_2D import Vec2D, Line2D, Arc2D

import matplotlib.pyplot as plt
import numpy as np

def draw_line_2D(x0: int, y0: int, x1: int, y1: int):

    v0 = Vec2D(x0, y0)
    v1 = Vec2D(x1, y1)
    line = Line2D(v0, v1)

    return line

def draw_arc_2D(x_start: int, y_start: int, x_center: int, y_center: int, angle_deg: float):

    start = Vec2D(x_start, y_start)
    center = Vec2D(x_center, y_center)
    arc = Arc2D(start, center, angle_deg)

    return arc

def draw_curves_2D(curves: list):

    for curve in curves:
        t_values = np.linspace(0, 1, 100) #this is basically the resolution of the drawing
        x_values = [curve.parametric(t).x for t in t_values]
        y_values = [curve.parametric(t).y for t in t_values]

        if isinstance(curve, Line2D):
            plt.plot(x_values, y_values, color='blue')
        elif isinstance(curve, Arc2D):
            plt.plot(x_values, y_values, color='red')

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("2D Plot")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    

def custom_toolpath_2D():
    curves = []

    curves.append(draw_line_2D(5, 5, -5, 5))
    curves.append(draw_arc_2D(-5, 5, -5, 3, 180))
    curves.append(draw_line_2D(-5, 1, 5, 1))
    curves.append(draw_arc_2D(5, 1, 5, 0, -90))
    curves.append(draw_line_2D(6, 0, 6, -2))
    curves.append(draw_arc_2D(6, -2, 5, -2, -90))
    curves.append(draw_line_2D(5, -3, -5, -3))


    draw_curves_2D(curves)

def canned_toolpath_2D(start_x: float, start_y: float, length: float, step: float, turns: int):

    curves = []

    start_pattern = Vec2D(start_x, start_y)
    start_pattern_1 = Vec2D(start_x - length, start_y)

    arc_offset = Vec2D(0, step / 2)
    line_offset = Vec2D(length, 0)

    curves.append(Line2D(start_pattern, start_pattern_1))

    right_turn = True

    for turn in range(turns):
        if right_turn == True:
            last_pos_vector = curves[-1].parametric(1)
            curves.append(Arc2D(last_pos_vector, last_pos_vector - arc_offset, 180))
            last_pos_vector = curves[-1].parametric(1)
            curves.append(Line2D(last_pos_vector, last_pos_vector + line_offset))
            right_turn = False

        elif right_turn == False:
            last_pos_vector = curves[-1].parametric(1)
            curves.append(Arc2D(last_pos_vector, last_pos_vector - arc_offset, -180))
            last_pos_vector = curves[-1].parametric(1)
            curves.append(Line2D(last_pos_vector, last_pos_vector - line_offset))
            right_turn = True
        
            
    draw_curves_2D(curves)






