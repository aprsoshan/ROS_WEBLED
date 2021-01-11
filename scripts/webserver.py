#! /usr/bin/python3
# -*- coding: utf-8 -*-
import http.server
import os
import rospy
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def kill():
        os.system("kill -KILL " + str(os.getpid()))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

os.chdir(os.path.dirname(__file__))
rospy.init_node("webserver")
rospy.on_shutdown(kill)
