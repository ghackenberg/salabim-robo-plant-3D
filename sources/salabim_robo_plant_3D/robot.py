import math

from salabim import Component, Animate3dSphere, Animate3dBar

from .vector import Vector

class Robot(Component):
    def __init__(self, position: Vector):
        
        # Constants

        self.position = position

        # Joints

        self.joints = list(
            map(
                lambda i: Animate3dSphere(
                    x=lambda t: self.calculate_joint_x_world(i, t),
                    y=lambda t: self.calculate_joint_y_world(i, t),
                    z=lambda t: self.calculate_joint_z_world(i, t),
                    radius=0.1,
                    color="green"
                ),
                range(4)
            )
        )
        
        # Bodies

        self.bodies = list(
            map(
                lambda i: Animate3dBar(
                    x0=lambda t: self.calculate_joint_x_world(i + 0, t),
                    y0=lambda t: self.calculate_joint_y_world(i + 0, t),
                    z0=lambda t: self.calculate_joint_z_world(i + 0, t),
                    x1=lambda t: self.calculate_joint_x_world(i + 1, t),
                    y1=lambda t: self.calculate_joint_y_world(i + 1, t),
                    z1=lambda t: self.calculate_joint_z_world(i + 1, t),
                    bar_width=0.1,
                    color="white"
                ),
                range(3)
            )
        )
    
    def calculate_joint_x_world(self, i: int, time: float):
        return self.position.x

    def calculate_joint_y_world(self, i: int, time: float):
        return self.position.y

    def calculate_joint_z_world(self, i: int, time: float):
        return self.position.z + i * 0.5