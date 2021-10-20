# Installation

1. Setup
```bash
source /opt/ros/noetic/setup.bash
cd ~/catkin_ws/src
git clone https://github.com/jonboiser/inorbit_demo.git
cd ~/catkin_ws
catkin_make
```
1. Install InOrbit agent
1. Change custom scripts location

```bash
printf '\nexport INORBIT_ACTIONS_PATH="%s/user-scripts"\n' $(pwd) >> ~/.inorbit/local/agent.env.sh
```
4. Start `roscore` in one terminal
1. Run this app in another terminal

```
source ~/catkin_ws/devel/setup.bash
```
