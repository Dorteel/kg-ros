import rospy
from std_msgs.msg import String
from rdflib import Graph

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    i = 0
    while not rospy.is_shutdown():
        
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i+=1

if __name__ == '__main__':

    # Create a Graph
    g = Graph()

    # Parse in an RDF file hosted on the Internet
    #g.parse("http://www.w3.org/People/Berners-Lee/card")

    g.parse("/home/user/catkin_ws/src/beginner_tutorials/scripts/test.tsv")

    hello_str = f"Graph g has {len(g)} statements."

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
