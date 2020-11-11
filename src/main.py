import rospy
from std_msgs.msg import String
from time import sleep
from roscam_sensors.msg import DHT22


if __name__ == "__main__":
    try:
        pub = rospy.Publisher("DHT22_sensor", DHT22, queue_size=10)
        rospy.init_node("DHT22_node", anonymous=True)
        rate = rospy.Rate(0.5)  # 10hz

        while not rospy.is_shutdown():

            msg_to_send = DHT22()
            msg_to_send.temperature = 1.2
            msg_to_send.humidity = 55

            rospy.loginfo(msg_to_send.temperature)
            rospy.loginfo(msg_to_send.humidity)

            pub.publish(msg_to_send)

            rate.sleep()

    except KeyboardInterrupt:
        print("Keyboard interrupt")
        rospy.signal_shutdown("stop program")

    except Exception as ex:
        print(ex)
        rospy.signal_shutdown("stop program")
