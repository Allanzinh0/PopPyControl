from pypot.creatures import PoppyHumanoid

poppy = PoppyHumanoid(simulator = 'vrep')

for motor in poppy.motors:
    motor.complient = False

# Dar uma pequena agaichada antes do dab
poppy.l_knee_y.goto_position(30, 1, wait=False)
poppy.r_knee_y.goto_position(30, 1, wait=False)

poppy.l_hip_y.goto_position(-15, 1, wait=False)
poppy.r_hip_y.goto_position(-15, 1, wait=False)

poppy.l_ankle_y.goto_position(-15, 1, wait=False)
poppy.r_ankle_y.goto_position(-15, 1, wait=True)

# Braco esquerdo
poppy.l_shoulder_x.goto_position(15, 0.5, wait=False)
poppy.l_shoulder_y.goto_position(-45, 0.5, wait=False)
poppy.l_elbow_y.goto_position(-110, 0.5, wait=False)
poppy.l_shoulder_x.goto_position(-5, 1, wait=False)
poppy.l_arm_z.goto_position(-60, 1, wait=False)
poppy.l_shoulder_y.goto_position(-80, 1, wait=False)

# Braco direito
poppy.r_shoulder_x.goto_position(-125, 1, wait=False)

poppy.head_y.goto_position(30, 1, wait=True)

