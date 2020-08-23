from manimlib.imports import *
import numpy as np

class SurfaceAnim(ThreeDScene):
        def construct (self):
                grid = NumberPlane().set_opacity(0.2).shift(-2*OUT)

                frame = self.camera.frame
                light = self.camera.light_source
                light.move_to([-25, -20, 20])

                sphere1 = Sphere().set_color(RED).scale(0.2).move_to(1*RIGHT + 1*UP - 2*OUT)
                sphere2 = sphere1.copy().move_to(-1*RIGHT + 1*UP - 2*OUT)

                sphere3 = sphere1.copy().move_to(-1*RIGHT + -1*UP - 2*OUT)
                sphere4 = sphere1.copy().move_to(1*RIGHT + -1*UP - 2*OUT)
                sphere5 = sphere1.copy().move_to(2*RIGHT + 2*UP + -2*OUT)
                sphere6 = sphere1.copy().move_to(-2*RIGHT + 2*UP + -2*OUT)
                sphere7 = sphere1.copy().move_to(-2*RIGHT + -2*UP + -2*OUT)
                sphere8 = sphere1.copy().move_to(2*RIGHT + -2*UP + -2*OUT)
                
                spheres = SGroup(sphere1,sphere2,sphere3,sphere4,sphere5,sphere6,sphere7,sphere8)

                line1 = self.getline(sphere1,sphere2)
                line1.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere1,sphere2)
                        )
                )
                
                line2 = self.getline(sphere2,sphere3)
                line2.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere2,sphere3)
                        )
                )
                line3 = self.getline(sphere3,sphere4)
                line3.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere3,sphere4)
                        )
                )
                line4 = self.getline(sphere4,sphere1)
                line4.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere4,sphere1)
                        )
                )

                line5 = self.getline(sphere5,sphere6)
                line5.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere5,sphere6)
                        )
                )
                line6 = self.getline(sphere6,sphere7)
                line6.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere6,sphere7)
                        )
                )
                line7 = self.getline(sphere7,sphere8)
                line7.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere7,sphere8)
                        )
                )
                line8 = self.getline(sphere8,sphere5)
                line8.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere8,sphere5)
                        )
                )

                line9 = self.getline(sphere1,sphere5)
                line9.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere1,sphere5)
                        )
                )
                line10 = self.getline(sphere2,sphere6)
                line10.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere2,sphere6)
                        )
                )
                line11 = self.getline(sphere3,sphere7)
                line11.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere3,sphere7)
                        )
                )
                line12 = self.getline(sphere4,sphere8)
                line12.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere4,sphere8)
                        )
                )

                lines = SGroup(line1,line2,line3,line4,
                        line5,line6,line7,line8,
                        line9,line10,line11,line12)
                
                #CUBE B

                sphereb1 = Sphere().set_color(BLUE).scale(0.2).move_to(2*RIGHT + 2*UP + 2*OUT)
                sphereb2 = sphereb1.copy().move_to(-2*RIGHT + 2*UP + 2*OUT)
                sphereb3 = sphereb1.copy().move_to(-2*RIGHT + -2*UP + 2*OUT)
                sphereb4 = sphereb1.copy().move_to(2*RIGHT + -2*UP + 2*OUT)
                sphereb5 = sphereb1.copy().move_to(2*RIGHT + 2*UP + -2*OUT)
                sphereb6 = sphereb1.copy().move_to(-2*RIGHT + 2*UP + -2*OUT)
                sphereb7 = sphereb1.copy().move_to(-2*RIGHT + -2*UP + -2*OUT)
                sphereb8 = sphereb1.copy().move_to(2*RIGHT + -2*UP + -2*OUT)

                spheresb = SGroup(sphereb1,sphereb2,sphereb3,sphereb4,
                        sphereb5,sphereb6,sphereb7,sphereb8)

                lineb1 = self.getline(sphereb1,sphereb2)
                lineb1.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb1,sphereb2)
                        )
                )
                lineb2 = self.getline(sphereb2,sphereb3)
                lineb2.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb2,sphereb3)
                        )
                )
                lineb3 = self.getline(sphereb3,sphereb4)
                lineb3.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb3,sphereb4)
                        )
                )
                lineb4 = self.getline(sphereb4,sphereb1)
                lineb4.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb4,sphereb1)
                        )
                )

                lineb5 = self.getline(sphereb5,sphereb6)
                lineb5.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb5,sphereb6)
                        )
                )
                lineb6 = self.getline(sphereb6,sphereb7)
                lineb6.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb6,sphereb7)
                        )
                )
                lineb7 = self.getline(sphereb7,sphereb8)
                lineb7.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb7,sphereb8)
                        )
                )
                lineb8 = self.getline(sphereb8,sphereb5)
                lineb8.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb8,sphereb5)
                        )
                )

                lineb9 = self.getline(sphereb1,sphereb5)
                lineb9.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb1,sphereb5)
                        )
                )
                lineb10 = self.getline(sphereb2,sphereb6)
                lineb10.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb2,sphereb6)
                        )
                )
                lineb11 = self.getline(sphereb3,sphereb7)
                lineb11.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb3,sphereb7)
                        )
                )
                lineb12 = self.getline(sphereb4,sphereb8)
                lineb12.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphereb4,sphereb8)
                        )
                )

                linesb = SGroup(lineb1,lineb2,lineb3,lineb4,
                        lineb5,lineb6,lineb7,lineb8,
                        lineb9,lineb10,lineb11,lineb12)

                #CONNECTOR

                linec1 = self.getline(sphere1,sphereb1)
                linec1.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere1,sphereb1)
                        )
                )
                linec2 = self.getline(sphere2,sphereb2)
                linec2.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere2,sphereb2)
                        )
                )
                linec3 = self.getline(sphere3,sphereb3)
                linec3.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere3,sphereb3)
                        )
                )
                linec4 = self.getline(sphere4,sphereb4)
                linec4.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere4,sphereb4)
                        )
                )

                linec5 = self.getline(sphere5,sphereb5)
                linec5.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere5,sphereb5)
                        )
                )
                linec6 = self.getline(sphere6,sphereb6)
                linec6.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere6,sphereb6)
                        )
                )
                linec7 = self.getline(sphere7,sphereb7)
                linec7.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere7,sphereb7)
                        )
                )
                linec8 = self.getline(sphere8,sphereb8)
                linec8.add_updater(
                        lambda mob: mob.become(
                        self.getline(sphere8,sphereb8)
                        )
                )

                linesc = SGroup(linec1,linec2,linec3,linec4,
                        linec5,linec6,linec7,linec8)

                self.play(ShowCreation(lines),ShowCreation(spheres),ShowCreation(grid))
                self.play(
                        ApplyMethod(
                        frame.set_rotation, -20 * DEGREES, 75 * DEGREES,
                        run_time=3
                ))
                frame.add_updater(lambda m, dt: m.increment_theta(dt *4 * DEGREES))
                #self.play(ShowCreation(line1))
                #self.play(FadeIn(sphere1),FadeIn(sphere2))
                
                posisi = np.array([[2,2,2],
                                [-2,2,2],
                                [-2,-2,2],
                                [2,-2,2]])
                                
                self.play(
                        sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3]
                )

                self.play(FadeOut(grid))

                self.play(
                        ReplacementTransform(lines.copy(),linesb),
                        ReplacementTransform(sphere1.copy(),sphereb1),
                        ReplacementTransform(sphere2.copy(),sphereb2),
                        ReplacementTransform(sphere3.copy(),sphereb3),
                        ReplacementTransform(sphere4.copy(),sphereb4),
                        ReplacementTransform(sphere5.copy(),sphereb5),
                        ReplacementTransform(sphere6.copy(),sphereb6),
                        ReplacementTransform(sphere7.copy(),sphereb7),
                        ReplacementTransform(sphere8.copy(),sphereb8)
                )
                self.add(linesc)

                #Moving the blue sphere
                posisib = np.array([[1,1,1],
                                [-1,1,1],
                                [-1,-1,1],
                                [1,-1,1],
                                [1,1,-1],
                                [-1,1,-1],
                                [-1,-1,-1],
                                [1,-1,-1]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],

                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7]
                )
                
                self.wait()

                posisib = np.array([[1,1,2],
                                [-1,1,2],
                                [-1,-1,2],
                                [1,-1,2],
                                [1,1,-2],
                                [-1,1,-2],
                                [-1,-1,-2],
                                [1,-1,-2]
                                ])

                posisi = np.array([[2,2,1],
                                [-2,2,1],
                                [-2,-2,1],
                                [2,-2,1],
                                [2,2,-1],
                                [-2,2,-1],
                                [-2,-2,-1],
                                [2,-2,-1]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],
                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7],

                        sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3],
                        sphere5.move_to,posisi[4],
                        sphere6.move_to,posisi[5],
                        sphere7.move_to,posisi[6],
                        sphere8.move_to,posisi[7],
                        rate_func=smooth
                )

                #ChangePosition
                
                posisib = np.array([[2,2,2],
                                [-2,2,2],
                                [-2,-2,2],
                                [2,-2,2],
                                [2,2,-2],
                                [-2,2,-2],
                                [-2,-2,-2],
                                [2,-2,-2]
                                ])

                posisi = np.array([[1,1,1],
                                [-1,1,1],
                                [-1,-1,1],
                                [1,-1,1],
                                [1,1,-1],
                                [-1,1,-1],
                                [-1,-1,-1],
                                [1,-1,-1]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],
                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7],

                        sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3],
                        sphere5.move_to,posisi[4],
                        sphere6.move_to,posisi[5],
                        sphere7.move_to,posisi[6],
                        sphere8.move_to,posisi[7],
                        
                        rate_func=smooth
                )
                self.wait(5)

                #ChangePosition
                
                posisi = np.array([[1,1,2],
                                [-1,1,2],
                                [-1,-1,2],
                                [1,-1,2],
                                [1,1,-2],
                                [-1,1,-2],
                                [-1,-1,-2],
                                [1,-1,-2]
                                ])

                posisib = np.array([[2,2,1],
                                [-2,2,1],
                                [-2,-2,1],
                                [2,-2,1],
                                [2,2,-1],
                                [-2,2,-1],
                                [-2,-2,-1],
                                [2,-2,-1]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],
                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7],

                        sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3],
                        sphere5.move_to,posisi[4],
                        sphere6.move_to,posisi[5],
                        sphere7.move_to,posisi[6],
                        sphere8.move_to,posisi[7],
                        rate_func=smooth
                )
                
                #ChangePosition
                
                posisi = np.array([[2,2,2],
                                [-2,2,2],
                                [-2,-2,2],
                                [2,-2,2],
                                [2,2,-2],
                                [-2,2,-2],
                                [-2,-2,-2],
                                [2,-2,-2]
                                ])

                posisib = np.array([[1,1,1],
                                [-1,1,1],
                                [-1,-1,1],
                                [1,-1,1],
                                [1,1,-1],
                                [-1,1,-1],
                                [-1,-1,-1],
                                [1,-1,-1]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],
                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7],

                        sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3],
                        sphere5.move_to,posisi[4],
                        sphere6.move_to,posisi[5],
                        sphere7.move_to,posisi[6],
                        sphere8.move_to,posisi[7],
                        
                        rate_func=smooth
                )

                

                ##### Iteration

                posisib = np.array([[1,1,2],
                                [-1,1,2],
                                [-1,-1,2],
                                [1,-1,2],
                                [1,1,-2],
                                [-1,1,-2],
                                [-1,-1,-2],
                                [1,-1,-2]
                                ])

                posisi = np.array([[2,2,1],
                                [-2,2,1],
                                [-2,-2,1],
                                [2,-2,1],
                                [2,2,-1],
                                [-2,2,-1],
                                [-2,-2,-1],
                                [2,-2,-1]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],
                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7],

                        sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3],
                        sphere5.move_to,posisi[4],
                        sphere6.move_to,posisi[5],
                        sphere7.move_to,posisi[6],
                        sphere8.move_to,posisi[7],
                        rate_func=smooth
                )

                #ChangePosition
                
                posisib = np.array([[2,2,2],
                                [-2,2,2],
                                [-2,-2,2],
                                [2,-2,2],
                                [2,2,-2],
                                [-2,2,-2],
                                [-2,-2,-2],
                                [2,-2,-2]
                                ])

                posisi = np.array([[1,1,1],
                                [-1,1,1],
                                [-1,-1,1],
                                [1,-1,1],
                                [1,1,-1],
                                [-1,1,-1],
                                [-1,-1,-1],
                                [1,-1,-1]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],
                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7],

                        sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3],
                        sphere5.move_to,posisi[4],
                        sphere6.move_to,posisi[5],
                        sphere7.move_to,posisi[6],
                        sphere8.move_to,posisi[7],
                        
                        rate_func=smooth
                )

                self.wait(5)
                #ChangePosition

                posisi = np.array([[1,1,2],
                                [-1,1,2],
                                [-1,-1,2],
                                [1,-1,2],
                                [1,1,-2],
                                [-1,1,-2],
                                [-1,-1,-2],
                                [1,-1,-2]
                                ])

                posisib = np.array([[2,2,1],
                                [-2,2,1],
                                [-2,-2,1],
                                [2,-2,1],
                                [2,2,-1],
                                [-2,2,-1],
                                [-2,-2,-1],
                                [2,-2,-1]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],
                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7],

                        sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3],
                        sphere5.move_to,posisi[4],
                        sphere6.move_to,posisi[5],
                        sphere7.move_to,posisi[6],
                        sphere8.move_to,posisi[7],
                        rate_func=smooth
                )
                
                #ChangePosition
                
                posisi = np.array([[2,2,2],
                                [-2,2,2],
                                [-2,-2,2],
                                [2,-2,2],
                                [2,2,-2],
                                [-2,2,-2],
                                [-2,-2,-2],
                                [2,-2,-2]
                                ])

                posisib = np.array([[1,1,1],
                                [-1,1,1],
                                [-1,-1,1],
                                [1,-1,1],
                                [1,1,-1],
                                [-1,1,-1],
                                [-1,-1,-1],
                                [1,-1,-1]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],
                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7],

                        sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3],
                        sphere5.move_to,posisi[4],
                        sphere6.move_to,posisi[5],
                        sphere7.move_to,posisi[6],
                        sphere8.move_to,posisi[7],
                        
                        rate_func=smooth
                )

                self.wait(5)

                posisib = np.array([[2,2,2],
                                [-2,2,2],
                                [-2,-2,2],
                                [2,-2,2],
                                [2,2,-2],
                                [-2,2,-2],
                                [-2,-2,-2],
                                [2,-2,-2]
                                ])

                self.play(
                        sphereb1.move_to,posisib[0],
                        sphereb2.move_to,posisib[1],
                        sphereb3.move_to,posisib[2],
                        sphereb4.move_to,posisib[3],
                        sphereb5.move_to,posisib[4],
                        sphereb6.move_to,posisib[5],
                        sphereb7.move_to,posisib[6],
                        sphereb8.move_to,posisib[7],
                        rate_func=smooth
                )

                self.play(FadeOut(spheresb),FadeOut(linesb),FadeOut(linesc))

                posisib = np.array([[1,1,-2],
                                [-1,1,-2],
                                [-1,-1,-2],
                                [1,-1,-2]
                                ])

                self.play(
                        sphere1.move_to,posisib[0],
                        sphere2.move_to,posisib[1],
                        sphere3.move_to,posisib[2],
                        sphere4.move_to,posisib[3],
                        ShowCreation(grid),
                        rate_func=smooth
                )

                self.play(
                        ApplyMethod(
                        frame.set_rotation, 0 * DEGREES, 0 * DEGREES,
                        run_time=3
                ))

                posisi = np.array([[0,0,0],
                                [0,0,0],
                                [0,0,0],
                                [0,0,0],
                                [0,0,0],
                                [0,0,0],
                                [0,0,0],
                                [0,0,0]
                                ])

                self.play(sphere1.move_to,posisi[0],
                        sphere2.move_to,posisi[1],
                        sphere3.move_to,posisi[2],
                        sphere4.move_to,posisi[3],
                        sphere5.move_to,posisi[4],
                        sphere6.move_to,posisi[5],
                        sphere7.move_to,posisi[6],
                        sphere8.move_to,posisi[7],
                        FadeOut(grid),        
                        rate_func=smooth
                )

                self.play(FadeOut(spheres))
                

        def getline(self,sphere1,sphere2):
                start_point = sphere1.get_center()
                end_point = sphere2.get_center()
                line = Line3D(
                        start_point,
                        end_point)
                return line
        

        
