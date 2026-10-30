from manim import *

class TransformGrid(Scene):
    def construct(self):
        background_plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 1
            },
            axis_config={"stroke_opacity": 1}
        )

        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 1
            }
        )

        vector = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(2, 2),
            buff=0,
            color=YELLOW
        )

        ghost = vector.copy()
        ghost.set_opacity(1)

        self.add(background_plane, plane, ghost, vector)
        self.wait(1)

        matrix = [[2, 0], [0, 1]]
        self.play(
            ApplyMatrix(matrix, plane),
            ApplyMatrix(matrix, vector),
            run_time=2
        )
        self.wait(1)