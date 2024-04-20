from manim import *


class Main(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        curve = ParametricFunction(
            lambda u: np.array([
                1 + u,
                3 * u,
                4 - (5 * u)
            ]), color=RED, t_range = np.array([0, 1, 0.001])
        ).set_shade_in_3d(True)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        dot_1 = Dot3D(point=axes.coords_to_point(1, 0, 4), radius=0.1, color=RED)
        dot_2 = Dot3D(point=axes.coords_to_point(2, 3, -1), radius=0.1, color=BLUE)
        dot_3 = Dot3D(point=[0, 1, -2], radius=0.1, color=ORANGE)
        self.add(dot_1, dot_2, dot_3)
        self.play(Write(axes))
        self.play(Create(curve))
        self.wait()

#manim -pql scene.py Main