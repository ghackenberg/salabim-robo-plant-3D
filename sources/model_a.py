from salabim import Environment, Animate3dGrid, inf
from salabim_robo_plant_3D import Conveyor, Robot, Vector

env = Environment()

env.animate(True)
env.width(1200)
env.height(600)
env.position((50, 50))

env.animate3d(True)
env.width3d(1200)
env.height3d(600)
env.position3d((100, 100))

env.view(x_eye=-5, y_eye=5, z_eye=5, x_center=0, y_center=0, z_center=0)

Animate3dGrid(x_range=range(-2,3), y_range=range(-2,3))

conveyorA = Conveyor()
conveyorB = Conveyor()

robotA = Robot(position=Vector( 0, 0,0))
robotB = Robot(position=Vector(+1,+1,0))
robotC = Robot(position=Vector(-1,-1,0))

env.run(inf)