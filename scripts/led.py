#!/usr/bin/env python3
import RPi.GPIO as GPIO
import rospy
import std_msgs.msg
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

def led_on(data):
    rospy.loginfo("LED ON")
    GPIO.output(25,GPIO.HIGH)

def led_off(data):
    rospy.loginfo("LED OFF")
    GPIO.output(25,GPIO.LOW)

if __name__ == '__main__':
    rospy.init_node('ledcontrol', anonymous=True)
    
    ledon = rospy.Subscriber("/ledon",std_msgs.msg.Int8, led_on)
    ledoff = rospy.Subscriber("/ledoff",std_msgs.msg.Int8, led_off)
    rospy.spin()










