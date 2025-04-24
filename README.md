## Robot Package Template

Using Ubuntu Server 24.04.01 on the raspberry pi 5
Using Ubuntu Server 24.04.02 on the other machine

##Setup
Install ROS and Dependencies

Pi Dependencies:
    ros-jazzy-control
    ros-jazzy-ros2-controllers
    
Other Machine Dependencies
    ros-jazzy-teleop-twist-keyboard
    ros-jazzy-control
    ros-jazzy-ros2-controllers

Install vex_interface into the Vex Controller.



##Run Sim Steps
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel_keyboard -p stamped:=true
ros2 launch robotics-project launch_sim.launch.py
rviz2
ros2 launch robotics-project online_async.launch.py use_sim_time:=true

Map the area and save / serialize it as obstacles_map

ros2 launch robotics-project localization.launch.py use_sim_time:=true
ros2 launch robotics-project navigation.launch.py use_sim_time:=true

##Run Robot Steps
Vex Controller: Launch the vex_interface application.
PI & PC at same time: sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"

PI: ros2 launch robotics-project launch_robot.launch.py 
PC: ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel_keyboard -p stamped:=true

PC: rviz2
PC: ros2 launch robotics-project online_async.launch.py

Map the area and save/serialize it as obstacles_map
PC: Stop online_async.launch.py

PC: ros2 launch robotics-project localization.launch.py
PC: ros2 launch robotics-project navigation.launch.py



###Thanks to
[Articulated Robotics](https://www.youtube.com/@ArticulatedRobotics) - Building a mobile robot series.