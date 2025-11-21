from data_structures_3D import Vec3D, Line3D, Helix3D

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.widgets import Slider

def draw_line_3D(x0: int, y0: int, z0: int, x1: int, y1: int, z1: int):

    v0 = Vec3D(x0, y0, z0)
    v1 = Vec3D(x1, y1, z1)
    line = Line3D(v0, v1)

    return line


def draw_helix_3D(radius: float, turns: float, height: float, x_center: int, y_center: int, z_center: int):

    center = Vec3D(x_center, y_center, z_center)
    helix = Helix3D(radius, turns, height, center)

    return helix

def draw_curves_3D(curves: list):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # Create 3D axes

    for curve in curves:
        t_values = np.linspace(0, 1, 100)
        x_values = [curve.parametric(t).x for t in t_values]
        y_values = [curve.parametric(t).y for t in t_values]
        z_values = [curve.parametric(t).z for t in t_values]

        if isinstance(curve, Line3D):
            ax.plot(x_values, y_values, z_values, color='blue')
        elif isinstance(curve, Helix3D):
            ax.plot(x_values, y_values, z_values, color='red')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Plot")
    ax.legend()
    plt.show()


def canned_toolpath_3D():
    curves = []

    curves.append(draw_helix_3D(4, 5, 10, 0, 0, 0))
    #curves.append(draw_line_3D(2, 3, 5, 5, 5, 5))

    draw_curves_3D(curves)


def draw_interactive_helix(helix):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.subplots_adjust(bottom=0.25)  # Make space for slider

    # Initial t value
    t_init = 1.0
    t_values = np.linspace(0, t_init, 100)
    x_values = [helix.parametric(t).x for t in t_values]
    y_values = [helix.parametric(t).y for t in t_values]
    z_values = [helix.parametric(t).z for t in t_values]

    # Plot initial helix
    [line] = ax.plot(x_values, y_values, z_values, color='red')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Interactive Helix")

    # Slider axis: [left, bottom, width, height]
    ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
    t_slider = Slider(ax_slider, 't', 0.01, 1.0, valinit=t_init, valstep=0.01)

    def update(val):
        t = t_slider.val
        t_values = np.linspace(0, t, 100)
        x_values = [helix.parametric(ti).x for ti in t_values]
        y_values = [helix.parametric(ti).y for ti in t_values]
        z_values = [helix.parametric(ti).z for ti in t_values]
        line.set_data(x_values, y_values)
        line.set_3d_properties(z_values)
        fig.canvas.draw_idle()

    t_slider.on_changed(update)
    plt.show()


def canned_interactive_toolpath():
    helix = draw_helix_3D(4, 5, 10, 0, 0, 0)
    draw_interactive_helix(helix)