from manimlib.imports import *

class Lorenz_Attractor(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=0,z_max=6,axis_config={"include_tip": True,"include_ticks":True,"stroke_width":1})
        dot = Sphere(radius=0.05,fill_color=BLUE).move_to(0*RIGHT + 0.1*UP + 0.105*OUT)
        
        self.set_camera_orientation(phi=65 * DEGREES,theta=30*DEGREES,gamma = 90*DEGREES)  
        self.begin_ambient_camera_rotation(rate=0.05)            #Start move camera

        dtime = 0.01
        numsteps = 30

        self.add(axes,dot)

        def lorenz(x, y, z, s=10, r=28, b=2.667):
            x_dot = s*(y - x)
            y_dot = r*x - y - x*z
            z_dot = x*y - b*z
            return x_dot, y_dot, z_dot

        def update_trajectory(self, dt):
            new_point = dot.get_center()
            if get_norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)

        traj = VMobject()
        traj.start_new_path(dot.get_center())
        traj.set_stroke(BLUE, 1.5, opacity=0.8)
        traj.add_updater(update_trajectory)
        self.add(traj)

        def update_position(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot.get_center()[0]*10, dot.get_center()[1]*10, dot.get_center()[2]*10)
            x = x_dot * dt/10
            y = y_dot * dt/10
            z = z_dot * dt/10
            self.shift(x/10*RIGHT + y/10*UP + z/10*OUT)

        dot.add_updater(update_position)
        self.wait(420)
