from manim import *
from math import sin


class Problem5(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # set axes
        labels = axes.get_axis_labels()
        dot_A = Dot3D(point=axes.coords_to_point(1, 0, 4), color=RED)
        dot_B = Dot3D(point=axes.coords_to_point(2, 3, -1), radius=0.1, color=BLUE)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        
        self.play(Write(axes), Write(labels))
        dots = AnimationGroup(Create(dot_A), Create(dot_B))
        self.play(dots)
        
        vectorA = Arrow3D(start=axes.coords_to_point(0, 0, 0), end=axes.coords_to_point(1, 0, 4))
        vectorB = Arrow3D(start=axes.coords_to_point(0, 0, 0), end=axes.coords_to_point(2, 3, -1))
        
        vectorBA = Arrow3D(axes.coords_to_point(0, 0, 0), axes.coords_to_point(1, 3, -5), color=GOLD)
        
        self.wait(4.0)

        transformBA = ApplyMethod(vectorBA.put_start_and_end_on, axes.coords_to_point(1, 0, 4),
                                  axes.coords_to_point(2, 3, -1))

        make_vectors_l1 = AnimationGroup(Create(vectorA), Create(vectorB))

        self.play(make_vectors_l1)
        self.play(Create(vectorBA))

        self.play(transformBA)

        self.wait()

        self.play(Uncreate(vectorA), Uncreate(vectorB))
        self.wait(4.0)
        lineAB = axes.plot_parametric_curve(lambda u: np.array([
            1 + u,
            3 * u,
            4 - (5 * u)
        ]), t_range=np.array([-3, 3, 0.001]), use_smoothing=False)
        
        self.play(Create(lineAB))

        self.play(Uncreate(vectorBA))

        self.wait(4.0)

        # done with problem 1

        # We found 2 points along the line, they are here:
        dot_D = Dot3D(point=axes.coords_to_point(4, -1, -1), color=GREEN)
        dot_E = Dot3D(point=axes.coords_to_point(7, 0, -3), color=PURPLE)
        
        self.wait(4.0)

        self.play(AnimationGroup(Create(dot_D), Create(dot_E)))

        # We won't show the vector thing again, but we'll just do the
        # arrows.

        vectorD = Arrow3D(start=axes.coords_to_point(0, 0, 0), end=axes.coords_to_point(4, -1, -1))
        vectorE = Arrow3D(start=axes.coords_to_point(0, 0, 0), end=axes.coords_to_point(7, 0, -3))

        vectorDE = Arrow3D(axes.coords_to_point(0, 0, 0), axes.coords_to_point(3, 1, -2), color=ORANGE)

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
        ]), t_range=np.array([-3, 3, 0.001]), use_smoothing=False)
        # self.add(line)
        self.play(Create(lineDE))
        self.play(Uncreate(vectorDE))
        
        self.wait(4.0)

        # rotate cam:
        self.move_camera(phi=90 * DEGREES, theta=0)
        self.wait(1)
        self.move_camera(phi=0, theta=0)
        self.wait(1)
        self.move_camera(phi=0, theta=90 * DEGREES)
        self.wait(1)

        self.move_camera(phi=75 * DEGREES, theta=-60 * DEGREES)

        # move along
        dotAB = Dot3D().set_color(ORANGE)

        dotDE = Dot3D().set_color(YELLOW)

        self.add(dotAB, dotDE)

        self.play(AnimationGroup(MoveAlongPath(dotAB, lineAB), rate_func = linear), MoveAlongPath(dotDE, lineDE, rate_func=linear))
        # Part C: solution

        # cross the 2 directions of the lines to find a plane
        # that should be able to intersect both
        # modifying it up and down is actually just parallel

        # first, the lines don't matter, so lets go back to the vectors.

        self.play(AnimationGroup(Uncreate(lineDE), Uncreate(lineAB)))
        
        self.wait(4.0)

        # make vector AB and DE v2, idk why i can't just recreate them

        vectorDEv2 = Arrow3D(axes.coords_to_point(4, -1, -1), axes.coords_to_point(7, 0, -3), color= ORANGE)

        vectorBAv2 = Arrow3D(axes.coords_to_point(1, 0, 4), axes.coords_to_point(2, 3, -1), color = BLUE)
        # show the vectors
        self.play(AnimationGroup(Create(vectorDEv2), Create(vectorBAv2)))

        # move vectors to center
        transformDECenter = ApplyMethod(vectorDEv2.put_start_and_end_on, axes.coords_to_point(0, 0, 0), axes.coords_to_point(3, 1, -2))

        transformBACenter = ApplyMethod(vectorBAv2.put_start_and_end_on, axes.coords_to_point(0, 0, 0), axes.coords_to_point(1, 3, -5))

        self.play(AnimationGroup(transformDECenter, transformBACenter, Uncreate(dot_A), Uncreate(dot_B), Uncreate(dot_D), Uncreate(dot_E)))
        
        self.wait(4.0)
       
        # show the normal that we get.
        vectorNorm = Arrow3D(axes.coords_to_point(0, 0, 0), axes.coords_to_point(1/13, 1, 8/13))

        self.play(Create(vectorNorm))
        self.wait(4.0)

        surface = Surface(
            lambda u, v: axes.coords_to_point(
                u,
                v,
                ((-1*u)+(-13*v))/8
            ),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(10, 10),
            checkerboard_colors=False,
            stroke_width = 0
        )
        surface.set_style(fill_opacity=0.7)
        surface.set_z_index(-20)
        vectorDEv2.set_z_index(0)
        axes.set_z_index(0)
        vectorBAv2.set_z_index(0)
        
        self.wait(4.0)

        surface2 = Surface(
            lambda u, v: axes.coords_to_point(
                u,
                v,
                (-3 + ((-1 * u) + (-13 * v))) / 8
            ),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(10, 10),
            checkerboard_colors=False,
            stroke_width=0
        )
        surface2.set_style(fill_opacity=0.7)
        self.play(Create(surface))
        surface2.match_depth(axes)
        surface2.set_z_index(-20)
        print(self.mobjects)
        
        self.wait(4.0)

        dot_C = Dot3D(axes.c2p(
            0,
            1,
            -2
        ), color=BLUE)
        dot_C.set_z_index(0)

        self.play(Create(dot_C))

        self.wait()
        self.play(Transform(surface, surface2))
        self.wait()

        self.play(AnimationGroup(Uncreate(surface), Uncreate(dot_C), Uncreate(vectorBAv2), Uncreate(vectorDEv2), Uncreate(vectorNorm)))
       
        
        axes2 = ThreeDAxes(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            z_range=[-20, 10, 1]
        )
        
        labels2 = axes2.get_axis_labels()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        self.play(AnimationGroup(Transform(axes, axes2), Transform(labels, labels2)))
        self.wait()
        
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
        
        self.wait()

#manim -pql test.py Problem5