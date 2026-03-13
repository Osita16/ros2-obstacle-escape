# 🤖 ROS2- Obstacle escape

## 🌌 Introduction

In the early stages of building autonomous robots, every journey begins with a simple instinct: **survival**.

This project implements a **reactive obstacle avoidance robot using ROS2 Humble**. The robot continuously reads **LiDAR sensor data** and makes real-time decisions to navigate its environment while avoiding collisions.

Instead of complex planning algorithms or global maps, this system follows a simple but powerful principle:

**Sense the world → React instantly → Keep moving forward.**

Think of it as the **first survival reflex of a robot**.

Before robots can build maps, recognize objects, or plan long paths, they must first learn one essential skill:

**How not to crash.**

---

## ⚙️ System Overview

The robot performs **reactive navigation** using LiDAR data.

### Workflow

1. LiDAR scans the surrounding environment  
2. Distance data is analyzed in real time  
3. If an obstacle is detected within a threshold distance  
4. The robot changes direction to avoid collision  
5. Movement continues until the next obstacle appears  

This creates a simple **sense-and-react behaviour**, similar to the reflexes of living organisms.

---

## 🛠️ Technologies Used

- **ROS2 Humble**
- **Python / rclpy**
- **LiDAR sensor data**
- **TurtleBot3**
- **Gazebo Simulation**

---

## 🎥 Demo

![Demo](demo/demo.gif)

You can record the simulation using:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
