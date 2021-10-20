#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String

def start_mock_app():
    global start_counting
    num_kits = 0
    start_counting = False

    pub = rospy.Publisher('inorbit/custom_data/0', String, queue_size=10)

    def pub_status(status):
        pub.publish(f"app_status={status}")

    def callback(data):
        global start_counting
        cmd_msg = data.data

        if cmd_msg == 'start':
            pub_status('start_pending')
            time.sleep(10)
            pub_status('running')
            start_counting = True
        elif cmd_msg == 'pause':
            pub_status('pause_pending')
            time.sleep(10)
            pub_status('paused')
            start_counting = False
        elif cmd_msg == 'stop':
            pub_status('stop_pending')
            time.sleep(10)
            pub_status('stopped')
            start_counting = False

    rospy.init_node('mock_app', anonymous=True)

    rospy.Subscriber('mock_app_cmds', String, callback)

    while not rospy.is_shutdown():
        if start_counting:
            num_kits += 1
            pub.publish('num_kits=%s' % num_kits)
        time.sleep(3)

if __name__ == '__main__':
    start_mock_app()
