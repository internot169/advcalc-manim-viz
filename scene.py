from manim import *
from math import sin


class Main(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-15 * DEGREES)
        
        '''
        line = axes.plot_parametric_curve(lambda u: np.array([
                1+u,
                3*u,
                4-(5*u)
            ]), use_smoothing = False)
        self.add(line)
        curve = ParametricFunction(
            lambda u: np.array([
                1+u,
                3*u,
                4-(5*u)
            ]), color = RED,  use_smoothing = False
        ).set_shade_in_3d(True)
        self.play(Create(curve))
        self.play(Unwrite(axes), Unwrite(labels))
        self.begin_ambient_camera_rotation(rate=0.1)     
        '''
        
        axes = ThreeDAxes()
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")
        
        self.play(Write(axes), Write(labels))
        
        #Problem A
        
        dot_1 = Dot3D(point=axes.coords_to_point(1, 0, 4), radius=0.1, color=RED)
        dot_2 = Dot3D(point=axes.coords_to_point(2, 3, -1), radius=0.1, color=BLUE)
        dot_3 = Dot3D(point=[0, 1, -2], radius=0.1, color=ORANGE)
        
        
        line = axes.plot_parametric_curve(
            lambda u: np.array([
                1 + u,
                3 * u,
                4 - (5 * u)
            ]), color=RED, t_range = np.array([0, 1, 0.001])
        ).set_shade_in_3d(True)
        
        self.add(dot_1, dot_2)
        self.add(line)
        self.wait(7.0)
        self.play(Unwrite(dot_1), Unwrite(dot_2), Unwrite(axes), Unwrite(labels))
        self.remove(line)
        
        # Problem B
        eq1 = Tex(r"$\frac{x-1}{3} = y+2 = \frac{z-1}{-2}$", font_size=96)
        self.add(eq1)
        self.wait(4.0)
        self.remove(eq1)
        
        self.play(Write(axes), Write(labels))
        
        dot_4 = Dot3D(point=axes.coords_to_point(4, -1, -1), radius=0.1, color=GREEN)
        dot_5 = Dot3D(point=axes.coords_to_point(7, 0, -1), radius=0.1, color=PURPLE)
        self.add(dot_4, dot_5)
        
        line2 = axes.plot_parametric_curve(
            lambda u: np.array([
                4+(3*u),
                -1+u,
                -1-(2*u)
            ]), color=RED, t_range = np.array([0, 1, 0.001])
        ).set_shade_in_3d(True)
        self.add(line)
        self.add(line2)
        self.wait(7.0)
        
        self.wait()
        
#manim -pql scene.py Main