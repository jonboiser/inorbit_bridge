# Installation

1. Setup
```bash
source /opt/ros/noetic/setup.bash
git clone` this repo to `~/Code/catkin_ws/src`, then `catkin_make`
```
1. Install InOrbit agent
1. Change custom scripts location

```bash
# this will override the previous export
echo "\nexport INORBIT_ACTIONS_PATH=\"$(pwd)/user_scripts\"" >> ~/.inorbit/local/agent.env.sh
```
4. Start `roscore` in one terminal
1. Run this app in another terminal

```
source ~/Code/catkin_ws/src/
```
