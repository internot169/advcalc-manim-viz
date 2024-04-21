from manim import *
from math import sin


class GraphExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # set axes
        labels = axes.get_axis_labels()
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.0 + u,
                3.0 * u,
                4.0 - (5.0 * u)
            ]), color=RED, t_range=np.array([0, 1, 0.001])
        ).set_shade_in_3d(True)
        dot_A = Dot3D(point=axes.coords_to_point(1, 0, 4), color=RED)
        dot_B = Dot3D(point=axes.coords_to_point(2, 3, -1), radius=0.1, color=BLUE)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        # self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Write(axes), Write(labels))
        dots = AnimationGroup(Create(dot_A), Create(dot_B))
        self.play(dots)

        vectorA = Arrow3D(start=axes.coords_to_point(0, 0, 0), end=axes.coords_to_point(1, 0, 4))
        vectorB = Arrow3D(start=axes.coords_to_point(0, 0, 0), end=axes.coords_to_point(2, 3, -1))

        vectorBA = Arrow3D(axes.coords_to_point(0, 0, 0), axes.coords_to_point(1, 3, -5))

        transformBA = ApplyMethod(vectorBA.put_start_and_end_on, axes.coords_to_point(1, 0, 4),
                                  axes.coords_to_point(2, 3, -1))

        make_vectors_l1 = AnimationGroup(Create(vectorA), Create(vectorB))

        self.play(make_vectors_l1)
        self.play(Create(vectorBA))

        self.play(transformBA)

        self.wait(1)

        self.play(Uncreate(vectorA), Uncreate(vectorB))

        lineAB = axes.plot_parametric_curve(lambda u: np.array([
            1 + u,
            3 * u,
            4 - (5 * u)
        ]), t_range=np.array([-1, 2, 0.001]), use_smoothing=False)
        # self.add(line)
        self.play(Create(lineAB))

        self.play(Uncreate(vectorBA))

        self.wait(2.0)

        # done with problem 1

        # We found 2 points along the line, they are here:
        dot_D = Dot3D(point=axes.coords_to_point(4, -1, -1), color=GREEN)
        dot_E = Dot3D(point=axes.coords_to_point(7, 0, -3), color=PURPLE)

        self.play(AnimationGroup(Create(dot_D), Create(dot_E)))

        # We won't show the vector thing again, but we'll just do the
        # arrows.

        vectorD = Arrow3D(start=axes.coords_to_point(0, 0, 0), end=axes.coords_to_point(4, -1, -1))
        vectorE = Arrow3D(start=axes.coords_to_point(0, 0, 0), end=axes.coords_to_point(7, 0, -3))

        vectorDE = Arrow3D(axes.coords_to_point(0, 0, 0), axes.coords_to_point(3, 1, -2))

        transformDE = ApplyMethod(vectorDE.put_start_and_end_on, axes.coords_to_point(4, -1, -1),
                                  axes.coords_to_point(7, 0, -3))

        self.play(AnimationGroup(Create(vectorD), Create(vectorE)))
        self.play(Create(vectorDE))
        self.play(transformDE)
        self.wait(1)
        self.play(AnimationGroup(Uncreate(vectorD), Uncreate(vectorE)))

        lineDE = axes.plot_parametric_curve(lambda u: np.array([
            4 + (3 * u),
            -1 + (1 * u),
            -1 + (-2 * u)
        ]), t_range=np.array([-1, 2, 0.001]), use_smoothing=False)
        # self.add(line)
        self.play(Create(lineDE))
        self.play(Uncreate(vectorDE))

        # rotate cam:
        self.move_camera(phi=90 * DEGREES, theta=0)
        self.wait(1)
        self.move_camera(phi=0, theta=0)
        self.wait(1)
        self.move_camera(phi=0, theta=90 * DEGREES)
        self.wait(1)

        # move along
        dotAB = Dot3D().set_color(ORANGE)

        dotDE = Dot3D().set_color(YELLOW)

        self.add(dotAB, dotDE)

        self.play(AnimationGroup(MoveAlongPath(dotAB, lineAB), rate_func = linear), MoveAlongPath(dotDE, lineDE, rate_func=linear))


        self.play(AnimationGroup(Uncreate(dot_A), Uncreate(dot_B), Uncreate(dot_D), Uncreate(dot_E)))
        self.play(Unwrite(axes), Unwrite(labels), Uncreate(lineAB), Uncreate(lineDE))
        # self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()
