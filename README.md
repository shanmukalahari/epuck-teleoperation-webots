# epuck-teleoperation-webots
Python based keyboard teleoperation and camera feedback for the epuck robot in webots.
# E-puck Teleoperation Controller using Webots

## 📌 Project Overview

This project implements a **keyboard-based teleoperation controller** for the e-puck mobile robot using Python in the Webots simulation environment.

The robot can be controlled remotely through keyboard inputs, allowing it to move forward, move backward, turn left, turn right, and stop. The e-puck's onboard camera provides live visual feedback from the robot's perspective.

## ✨ Features

- **Forward Movement:** Move the robot forward.
- **Backward Movement:** Move the robot backward.
- **Left Turn:** Rotate the robot to the left.
- **Right Turn:** Rotate the robot to the right.
- **Stop:** Stop both wheel motors.
- **Live Camera Feedback:** View the robot's surroundings through its onboard camera in Webots.

## 🎮 Keyboard Controls

| Key | Action |
|---|---|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Turn left |
| `D` | Turn right |
| `X` | Stop the robot |

The movement command remains active until another movement key or the stop key is pressed.

## 🛠️ Technologies Used

- Python
- Webots Robotics Simulator
- e-puck Mobile Robot
- Webots Robot and Keyboard APIs
- Webots Camera Device

## ⚙️ How to Run

1. Install and open Webots.
2. Open a world containing the e-puck robot.
3. Place the Python controller file in the appropriate Webots controller directory.
4. Assign `epuck_teleoperation` as the robot's controller.
5. Start the simulation.
6. Click inside the 3D simulation view to provide keyboard input.
7. Use `W`, `A`, `S`, `D`, and `X` to control the robot.
8. Enable the camera overlay in Webots to observe the robot's perspective.

## 📂 Project Structure

```text
epuck-teleoperation-webots/
├── README.md
├── epuck_teleoperation.py
├── your_world.wbt
└── screenshot.jpg
```

*Note: Replace `your_world.wbt` and `screenshot.jpg` with your actual filenames. The world file and screenshot are optional.*

## 🧪 Testing

The controller was tested in Webots to verify keyboard-based robot movement, stopping behavior, and camera operation.

## 🎯 Expected Outcome

A remotely controlled e-puck robot that responds to keyboard commands and provides live visual feedback through its onboard camera.

## 👩‍💻 Author

Created as part of a robotics class assignment.

---

**Project Status:** Implemented and tested in Webots.
