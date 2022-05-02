# Provides a template for ROS node

import rospy
from std_msgs.msg import String
from rdflib import Graph

class RosNode():
    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self, name="test_node"):

        # Initialize node
        self.node_name = name
        rospy.init_node(self.node_name)

        # Node cycle rate (in Hz).
        self.loop_rate = rospy.Rate(100)

        # Publishers
        self.publish_topic = "Test"
        self.msg_to_publish = "Hello"
        self.pub = rospy.Publisher(self.publish_topic, String, queue_size=100)

        # Subscribers
        self.subscribe_topic = "Test"
        rospy.Subscriber(self.subscribe_topic, String, self.callback)
        self.msg = "Hello"

    def callback(self, msg):
        self.msg = msg
        rospy.loginfo("Received: {}".format(self.msg.data))


    def start(self):
        while not rospy.is_shutdown():
            # Publish our custom message.
            if self.msg:
                self.msg_to_publish = self.msg
                self.pub.publish(self.msg_to_publish)
            self.loop_rate.sleep()