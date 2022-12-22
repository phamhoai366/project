killall gzserver and killall gzclient

#robot_description
roslaunch project robot_rviz.launch    -- open model in rviz

#robot_gazebo
roslaunch project robot_gazebo.launch  -- open model in world gazebo

#control robot
rosrun teleop_twist_keyboard teleop_twist_keyboard.py

#robot_slam

(open new terminal) roslaunch project robot_slam.launch

(open new terminal) rosrun teleop_twist_keyboard teleop_twist_keyboard.py

(open new terminal) rosrun map_server map_saver -f ~/map

#robot_navigation
roslaunch project robot_gazebo.launch

(open new terminal) roslaunch project robot_navigation.launch
or roslaunch project robot_navigation.launch dwa_local_planner:=true


#astar
roslaunch project astar.launch x_pos:=4.0 y_pos:=3.0 yaw:=3.142
1->0.6->3.0->2.0->4.0->3.0->3.142->-4.0->-3.0

#avoid object
roslaunch project robot_gazebo.launch
(open new terminal) rosrun project obstacle_avoidance.py
