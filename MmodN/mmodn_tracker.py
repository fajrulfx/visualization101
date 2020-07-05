from manimlib.imports import *

class MmodNTracker(Scene):
    CONFIG = {
        "number_of_lines": 400,
        "gradient_colors":[RED,YELLOW,BLUE],
        "end_value":100,
        "total_time":180,
    }
    def construct(self):
        circle = Circle().set_height(FRAME_HEIGHT*0.85)
        circle.to_edge(RIGHT,buff=1)
        mod_tracker = ValueTracker(0)
        lines = self.get_m_mod_n_objects(circle,mod_tracker.get_value())
        lines.add_updater(
            lambda mob: mob.become(
                self.get_m_mod_n_objects(circle,mod_tracker.get_value())
                )
            )

        ftext = TexMobject("f( ")
        ftext.scale(2)
        ftext.to_edge(LEFT,buff=1)

        decimal = DecimalNumber(
                0,
                num_decimal_places=0,
                include_sign=False,
                unit=None, 
            )
        decimal.scale(2)
        decimal.next_to(fungsi,RIGHT,buff=0)
        decimal.add_updater(lambda d: d.set_value(mod_tracker.get_value()))

        closetext = TexMobject("\\, ,400)")
        closetext.scale(2)
        closetext.add_updater(lambda m: m.next_to(decimal,RIGHT,buff=SMALL_BUFF))

        self.play(FadeIn(circle),FadeIn(lines),FadeIn(fungsi),FadeIn(decimal),FadeIn(akhir))
        self.play(
            mod_tracker.set_value,self.end_value,
            rate_func=linear,
            run_time=self.total_time
            )
        self.wait(5)

    def get_m_mod_n_objects(self,circle,x,y=None):
        if y==None:
            y = self.number_of_lines
        lines = VGroup()
        for i in range(y):
            start_point = circle.point_from_proportion((i%y)/y)
            end_point = circle.point_from_proportion(((i*x)%y)/y)
            line = Line(start_point,end_point).set_stroke(width=1)
            lines.add(line)
        lines.set_color_by_gradient(*self.gradient_colors)
        return lines
