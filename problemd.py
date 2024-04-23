from manim import *
from math import sin
import random


class GraphExample(ThreeDScene):
    def construct(self):
        #TODO For part 2: show the demo of how the direction vector matters
        axes2 = ThreeDAxes(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            z_range=[-20, 10, 1]
        )
        # set axes
        labels = axes2.get_axis_labels()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        self.play(Write(axes2), Write(labels))
        
        # Move the thing and also rotate
        surface3 = Surface(
            lambda u, v: axes2.c2p(
                12-u,
                u,
                v
                ),
            u_range=[-15, 15],
            v_range=[-15, 15],
            resolution=8,
            checkerboard_colors=False,
        )
        surface3.set_style(fill_opacity=0.7)
        
        self.play(Create(surface3))
        
        a = Dot3D(point=axes2.coords_to_point(8, 4, 1), color=GREEN)
        b = Dot3D(point=axes2.coords_to_point(6, 6, 0), color=RED)
        c = Dot3D(point=axes2.coords_to_point(3, 9, 1), color=PURPLE)
        self.play(AnimationGroup(Create(a), Create(b), Create(c)))
            
        self.wait(4.0)
        
        g = Arrow3D(start=axes2.coords_to_point(6, 6, 0), end=axes2.coords_to_point(8, 4, 1))
        e = Arrow3D(start=axes2.coords_to_point(6, 6, 0), end=axes2.coords_to_point(3, 9, 1))
        self.play(AnimationGroup(Create(g), Create(e)))
        self.play(AnimationGroup(Uncreate(a), Uncreate(b), Uncreate(c)))
        
        self.wait(4.0)
        
        f = Arrow3D(start=axes2.coords_to_point(6, 6, 0), end=axes2.coords_to_point(3, 3, 0))
        self.play(Create(f))
        
        self.wait(4.0)
        
        line2 = axes2.plot_parametric_curve(lambda u: np.array([
            3 + (2 * u),
            u,
            1 - u
        ]), t_range=np.array([-10, 10, 0.001]), use_smoothing=False)
        
        self.play(Create(line2))
        
        self.wait(4.0)
        
        d = Dot3D(point=axes2.coords_to_point(9, 3, -2))
        self.play(Create(d))
        
        self.wait(4.0)
        
        self.wait()

#manim -pql problemd.py GraphExample