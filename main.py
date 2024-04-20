from manim import *
from math import sin


class GraphExample(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: np.array([
                1+u,
                3*u,
                4-(5*u)
            ]), color = RED, t_range=np.array([-1 * TAU, 1 * TAU, 0.001])
        ).set_shade_in_3d(True)
        axes = ThreeDAxes()
        dot_1 = Dot3D(point=axes.coords_to_point(1, 0, 4), color=RED)
        dot_2 = Dot3D(point=axes.coords_to_point(2, 3, -1), radius=0.1, color=BLUE)
        dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-15 * DEGREES)
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")
        # self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Write(axes), Write(labels))
        self.add(axes, dot_1, dot_2, dot_3)

        # line = axes.plot_parametric_curve(lambda u: np.array([
        #         1+u,
        #         3*u,
        #         4-(5*u)
        #     ]), use_smoothing = False)
        # self.add(line)
        
        
        self.wait(4.0)

        self.play(Unwrite(axes), Unwrite(labels), Uncreate(curve1))
        # self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()