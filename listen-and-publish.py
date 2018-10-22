#!/home/kandre/src/sleepcycle/venv/bin/python3

from zeroconf import ServiceBrowser, Zeroconf
import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()

mqttc.connect("mqtt.ak-online.be")
mqttc.loop_start()

SleepCycle_mDNS_Service = "_sleepcycle_ald._tcp.local."

def publish( devicename, state):
    name = devicename.replace(".%s" % (SleepCycle_mDNS_Service), "")
    topic = "sleepcycle/%s" % (name)
    print("publishing to %s: %s" % (topic, state))
    mqttc.publish(topic, state)

class MyListener:

    def add_service(self, zeroconf, type, name):
        print("Service %s added" % (name))
        publish(name,"ON")

    def remove_service(self, zeroconf, type, name):
        print("Device %s removed" % (name,))
        publish(name,"OFF")



zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, SleepCycle_mDNS_Service, listener)

while True:
    time.sleep(100)

zeroconf.close()
mqttc.loop_stop()
