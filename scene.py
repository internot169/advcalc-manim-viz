from manim import *


class Main(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(Write(axes))
        self.wait()

#manim -pql scene.py Main