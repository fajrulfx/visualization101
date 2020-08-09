import numpy as np
from manimlib.imports import *

class ThreeDArrow(Line):
    CONFIG = {
        "tip_length": 0.3,
        "tip_width_to_length_ratio": 1,
        "max_tip_length_to_length_ratio": 0.35,
        "max_stem_width_to_tip_width_ratio": 0.3,
        "buff": 0,
        "propagate_style_to_family": False,
        "preserve_tip_size_when_scaling": True,
        "normal_vector": OUT,
        "use_rectangular_stem": True,
        "rectangular_stem_width": 0.05,
    }

    def __init__(self, *args, **kwargs):
        points = list(map(self.pointify, args))
        if len(args) == 1:
            args = (points[0] + UP + LEFT, points[0])
        Line.__init__(self, *args, **kwargs)
        self.add_tip()

    def add_tip(self, add_at_end=True):
        tip = VMobject(
            close_new_points=True,
            mark_paths_closed=True,
            fill_color=self.color,
            fill_opacity=1,
            stroke_color=self.color,
            stroke_width=0,
        )
        tip.add_at_end = add_at_end
        self.set_tip_points(tip, add_at_end, preserve_normal=False)
        self.add(tip)
        if not hasattr(self, 'tip'):
            self.tip = VGroup()
            self.tip.match_style(tip)
        self.tip.add(tip)
        return tip

    def set_tip_points(
        self, tip,
        add_at_end=True,
        tip_length=None,
        preserve_normal=True,
    ):
        if tip_length is None:
            tip_length = self.tip_length
        if preserve_normal:
            normal_vector = self.get_normal_vector()
        else:
            normal_vector = self.normal_vector
        line_length = get_norm(self.points[-1] - self.points[0])
        tip_length = min(
            tip_length, self.max_tip_length_to_length_ratio * line_length
        )

        indices = (-2, -1) if add_at_end else (1, 0)
        pre_end_point, end_point = [
            self.get_anchors()[index]
            for index in indices
        ]
        vect = end_point - pre_end_point
        perp_vect = np.cross(vect, normal_vector)
        for v in vect, perp_vect:
            if get_norm(v) == 0:
                v[0] = 1
            v *= tip_length / get_norm(v)
        ratio = self.tip_width_to_length_ratio
        tip.set_points_as_corners([
            end_point,
            end_point - vect + perp_vect * ratio / 2,
            end_point - vect - perp_vect * ratio / 2,
        ])

        return self

    def get_normal_vector(self):
        p0, p1, p2 = self.tip[0].get_anchors()[:3]
        result = np.cross(p2 - p1, p1 - p0)
        norm = get_norm(result)
        if norm == 0:
            return self.normal_vector
        else:
            return result / norm

    def reset_normal_vector(self):
        self.normal_vector = self.get_normal_vector()
        return self

    def get_end(self):
        if hasattr(self, "tip"):
            return self.tip[0].get_anchors()[0]
        else:
            return Line.get_end(self)

    def get_tip(self):
        return self.tip

    def put_start_and_end_on(self, *args, **kwargs):
        Line.put_start_and_end_on(self, *args, **kwargs)
        self.set_tip_points(self.tip[0], preserve_normal=False)
        self.set_rectangular_stem_points()
        return self

    def scale(self, scale_factor, **kwargs):
        Line.scale(self, scale_factor, **kwargs)
        if self.preserve_tip_size_when_scaling:
            for t in self.tip:
                self.set_tip_points(t, add_at_end=t.add_at_end)
        if self.use_rectangular_stem:
            self.set_rectangular_stem_points()
        return self

    def copy(self):
        return self.deepcopy()

class VectorDecomposition(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
        grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
        
        '''
        #This is an option to add 3D grids
        grids = VGroup()
        for i in range(1,2):
            grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
            grid2 = grid.copy()
            grid.shift(2*i*OUT)
            grid2.shift(-2*i*OUT)
            grids.add(grid,grid2)

        gridz = grids.copy().rotate(90*DEGREES,axis=RIGHT)
        '''

        sphere = Sphere(radius=0.1).move_to(3*RIGHT + 2*UP + 3*OUT)
        v0 = ThreeDArrow(ORIGIN,sphere.get_center(),color=BLUE)
        v1 = ThreeDArrow(ORIGIN,np.array((sphere.get_center()[0],0,0)),color=RED)
        v2 = ThreeDArrow(np.array((sphere.get_center()[0],0,0)),np.array((sphere.get_center()[0],sphere.get_center()[1],0)),color=YELLOW)
        v3 = ThreeDArrow(np.array((sphere.get_center()[0],sphere.get_center()[1],0)),sphere.get_center(),color=GREEN)

        def update_vector0(self):
            self.become(ThreeDArrow(ORIGIN,sphere.get_center(),color=BLUE))

        def update_vector1(self):
            self.become(ThreeDArrow(ORIGIN,np.array((sphere.get_center()[0],0,0)),color=RED))

        def update_vector2(self):
            self.become(ThreeDArrow(np.array((sphere.get_center()[0],0,0)),np.array((sphere.get_center()[0],sphere.get_center()[1],0)),color=YELLOW))

        def update_vector3(self):
            self.become(ThreeDArrow(np.array((sphere.get_center()[0],sphere.get_center()[1],0)),sphere.get_center(),color=GREEN))

        t = 0

        def update_position(self,dt):
            nonlocal t
            t += dt/2
            x = 2*np.sin(t)
            y = 3*np.cos(t)
            z = 3.5*np.sin(t+1.5)
            self.move_to(x*RIGHT+y*UP+z*OUT)

        v0.add_updater(update_vector0)
        v1.add_updater(update_vector1)
        v2.add_updater(update_vector2)
        v3.add_updater(update_vector3)
        sphere.add_updater(update_position)

        self.set_camera_orientation(phi=65 * DEGREES,theta=30*DEGREES)  
        self.add(sphere,v0,v1,v2,v3,axes,grid)         
        #self.play(ShowCreation(sphere),ShowCreation(garis),ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=0.1)            #Start move camera
        self.wait(60)

        
        
