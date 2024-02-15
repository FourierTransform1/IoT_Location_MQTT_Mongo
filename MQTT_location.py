import paho.mqtt.client as mqtt
import json
import time


#Initialise MQTT Broker
mqttBroker ="test.mosquitto.org"
client = mqtt.Client (client_id="location_simulator", clean_session=True)
client.connect(mqttBroker, port=1883)


#publish location information to MQTT Broker
# topic format :  org/id/location --string
# payload -- dict
def pub_device_location(topic, payload):
  client.publish(topic, json.dumps(payload))
  #time.sleep(1)
  return 


def shut_down():
   client.disconnect()

