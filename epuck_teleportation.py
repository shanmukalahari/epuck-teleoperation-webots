
from controller import Robot, Keyboard

# Create the robot
robot = Robot()

# Simulation time step
timestep = int(robot.getBasicTimeStep())

# Get the two wheel motors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Set motors to velocity control mode
left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

# Start with the robot stopped
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Enable keyboard input
keyboard = Keyboard()
keyboard.enable(timestep)

# Enable the e-puck camera
camera = robot.getDevice("camera")
camera.enable(timestep)

# Wheel speed (rad/s)
SPEED = 3.0

# Current movement command
command = "STOP"

print("E-puck Teleoperation Controller Started")
print("W = Forward, S = Backward")
print("A = Left, D = Right, X = Stop")

# Main control loop
while robot.step(timestep) != -1:

    key = keyboard.getKey()

    # Update the movement command
    if key == ord('W') or key == ord('w'):
        command = "FORWARD"

    elif key == ord('S') or key == ord('s'):
        command = "BACKWARD"

    elif key == ord('A') or key == ord('a'):
        command = "LEFT"

    elif key == ord('D') or key == ord('d'):
        command = "RIGHT"

    elif key == ord('X') or key == ord('x'):
        command = "STOP"

    # Apply wheel velocities
    if command == "FORWARD":
        left_motor.setVelocity(SPEED)
        right_motor.setVelocity(SPEED)

    elif command == "BACKWARD":
        left_motor.setVelocity(-SPEED)
        right_motor.setVelocity(-SPEED)

    elif command == "LEFT":
        left_motor.setVelocity(-SPEED)
        right_motor.setVelocity(SPEED)

    elif command == "RIGHT":
        left_motor.setVelocity(SPEED)
        right_motor.setVelocity(-SPEED)

    else:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
