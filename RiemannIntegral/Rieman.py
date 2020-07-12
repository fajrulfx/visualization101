# This code is still messy. I'll update soon to make it more clear.

from manimlib.imports import *
import numpy as np

class RiemannIntegral(GraphScene):
    CONFIG = {
        "x_max": 6,
        "x_min": -2,
        "x_labeled_nums": list(range(-2, 6)),
        "y_min": 0,
        "y_max": 2,
        "y_tick_frequency": 2.5,
        "y_labeled_nums": list(range(5, 20, 5)),
        "n_rect_iterations": 1,
        "default_right_x": 5,
        "func": lambda x: 0.1*math.pow(x-2, 2) + 1,
        "func2": lambda x: (-1* (x-3)**3 + 3*(x-3)+3)/15,
        "func3": lambda x: (math.sin(x/1.5)+1)/2,
        "func4": lambda x: (x/10+1),
        "func5": lambda x: np.exp(x)/25,
        "y_axis_label": "",
    }

    def construct(self):
        self.setup_axes()

        graph = self.get_graph(self.func)
        self.play(ShowCreation(graph))
        self.graph = graph

        rects = VGroup()

        t = TexMobject("(x-2)^2+1")
        t.scale(1.3)
        t.to_edge(RIGHT)

        self.play(FadeInFromDown(t))

        for dx in np.arange(0.2, 0.05, -0.05):
            rect = self.get_riemann_rectangles(
                self.graph,
                x_min=0,
                x_max=self.default_right_x,
                dx=dx,
                stroke_width=4*dx,
            )
            rects.add(rect)

        self.play(
            DrawBorderThenFill(
                rects[0],
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
        )
        self.wait()

        for rect in rects[1:]:
            self.play(
                Transform(
                    rects[0], rect,
                    run_time=2,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )

        self.play(FadeOut(rects[0]),FadeOut(t))

        #Graph2

        graph2 = self.get_graph(self.func2)
        self.play(Transform(graph,graph2))
        self.graph = graph2

        rects2 = VGroup()

        t = TexMobject("-(x-3)^3 + 3(x-3) + 3")
        t.scale(1.3)
        t.to_edge(RIGHT)

        self.play(FadeInFromDown(t))

        for dx in np.arange(0.2, 0.05, -0.05):
            rect2 = self.get_riemann_rectangles(
                self.graph,
                x_min=0,
                x_max=self.default_right_x,
                dx=dx,
                stroke_width=4*dx,
            )
            rects2.add(rect2)

        self.play(
            DrawBorderThenFill(
                rects2[0],
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
        )
        self.wait()

        for rect2 in rects2[1:]:
            self.play(
                Transform(
                    rects2[0], rect2,
                    run_time=2,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )

        self.play(FadeOut(rects2[0]),FadeOut(t))

        #Graph3

        graph3 = self.get_graph(self.func3)
        self.play(Transform(graph,graph3))
        self.graph = graph3

        rects3 = VGroup()

        t = TexMobject("\sin(\\frac{x}{2})+1")
        t.scale(1.3)
        t.to_edge(RIGHT)

        self.play(FadeInFromDown(t))

        for dx in np.arange(0.2, 0.05, -0.05):
            rect3 = self.get_riemann_rectangles(
                self.graph,
                x_min=0,
                x_max=self.default_right_x,
                dx=dx,
                stroke_width=4*dx,
            )
            rects3.add(rect3)

        self.play(
            DrawBorderThenFill(
                rects3[0],
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
        )
        self.wait()

        for rect3 in rects3[1:]:
            self.play(
                Transform(
                    rects3[0], rect3,
                    run_time=2,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )

        self.play(FadeOut(rects3[0]),FadeOut(t))

        #Graph4

        graph4 = self.get_graph(self.func4)
        self.play(Transform(graph,graph4))
        self.graph = graph4

        rects3 = VGroup()

        t = TexMobject("\\frac{x}{2}+2")
        t.scale(1.3)
        t.to_edge(RIGHT)

        self.play(FadeInFromDown(t))

        for dx in np.arange(0.2, 0.05, -0.05):
            rect3 = self.get_riemann_rectangles(
                self.graph,
                x_min=0,
                x_max=self.default_right_x,
                dx=dx,
                stroke_width=4*dx,
            )
            rects3.add(rect3)

        self.play(
            DrawBorderThenFill(
                rects3[0],
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
        )
        self.wait()

        for rect3 in rects3[1:]:
            self.play(
                Transform(
                    rects3[0], rect3,
                    run_time=2,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )

        self.wait()
        self.play(FadeOut(rects3[0]),FadeOut(t),FadeOut(graph))
