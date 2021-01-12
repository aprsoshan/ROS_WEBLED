# CONTRIBUTOR

(c) 2020 RyuichiUeda and SoutaNakamura

# ROSを用いた作品

2020年CITロボットシステム学課題２として作成したブラウザからLEDのON・OFFを制御できるパッケージです。

# インスト―ル方法

$ cd ~/catkin_ws/src/
$ git clone https://github.com/aprsoshan/ROS_WEBled.git
$ cd ..
$ catkin_make
# 実行方法
$ sudo apt install ros-catkin-rosbridge-suite
$ roscore
$ roslaunch rosbridge_server rosbridge_websocket.launch
$ rosrun ROS_WEBled webserver.py
$ rosrun ROS_WEBled led.py

# 説明

(Raspberry piのIP):8000にアクセスするとLEDONとLEDOFFのスイッチが表示される。

LEDON：LEDが点灯する。 LEDOFF：LEDが消灯する。

# 参考動画

https://youtu.be/KEljHJpgJUk

# 参考にした資料

2017年度ロボットシステム学授業資料https://github.com/ryuichiueda/robosys2018

# License

GPLv3 license
