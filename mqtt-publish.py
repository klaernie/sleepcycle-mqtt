#!python

from time import sleep
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()

mqttc.connect("mqtt.ak-online.be")
mqttc.loop_start()

mqttc.publish("sleepcycle/Klaernie iPhone", "ON")

sleep(10)
