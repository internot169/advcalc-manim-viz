from manim import *
from math import sin
import random


class GraphExample(ThreeDScene):
    def construct(self):
        #TODO For part 2: show the demo of how the direction vector matters
        axes = ThreeDAxes(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            z_range=[-20, 10, 1]
        )
        # set axes
        labels = axes.get_axis_labels()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        self.play(Write(axes), Write(labels))
        
        surface = Surface(
            lambda u, v: axes.c2p(
                12-u,
                u,
                v
                ),
            u_range=[-15, 15],
            v_range=[-15, 15],
            resolution=8,
        )
        
        self.play(Create(surface))
        
        a = Dot3D(point=axes.coords_to_point(8, 4, 1), color=GREEN)
        b = Dot3D(point=axes.coords_to_point(6, 6, 0), color=RED)
        c = Dot3D(point=axes.coords_to_point(3, 9, 1), color=PURPLE)
        self.play(AnimationGroup(Create(a), Create(b), Create(c)))
        
        self.wait(4.0)
        
        vectorD = Arrow3D(start=axes.coords_to_point(6, 6, 0), end=axes.coords_to_point(8, 4, 1))
        vectorE = Arrow3D(start=axes.coords_to_point(6, 6, 0), end=axes.coords_to_point(3, 9, 1))
        self.play(AnimationGroup(Create(vectorD), Create(vectorE)))
        
        self.wait(4.0)
        
        vectorF = Arrow3D(start=axes.coords_to_point(6, 6, 0), end=axes.coords_to_point(5, 5, 0))
        self.play(Create(vectorF))
        
        self.wait(4.0)
        
        line2 = axes.plot_parametric_curve(lambda u: np.array([
            3 + (2 * u),
            u,
            1 - u
        ]), t_range=np.array([-10, 10, 0.001]), use_smoothing=False)
        
        self.play(Create(line2))
        
        self.wait(4.0)
        
        d = Dot3D(point=axes.coords_to_point(9, 3, -2))
        self.play(Create(d))
        
        self.wait(4.0)
        
        self.wait()

#manim -pql problemd.py GraphExample