#!/bin/bash

source /opt/ros/noetic/setup.sh

rostopic pub -1 /mock_app_cmds std_msgs/String reset