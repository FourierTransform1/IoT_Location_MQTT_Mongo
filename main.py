import MQTT_location as mqtt_server
import THING as thing_
import time as time
import random


# create dummy devices for testing system
def create_dummies():
    
    things = [] #array storing all devices sending location information
    
    organisations = [100, 102, 103, 104, 107]   #list of org. numbers
    
    asset_types = ["car", "bus"]    #list of asset types
    
    for i in range(200): #creating Thing objects and adding to array
      asset = thing_.Thing(random.choice(organisations), random.choice(asset_types), i)
      asset.location = [60.16920526, 24.95115530 ]
      things.append(asset)

    return things

# get location with MongoDB query sent via MQTT 
def get_location(company, id):  
 topic = "{}/{}/find".format(company, id)   #unique find topic
 payload = {"org": company,
            "name": id,}
 mqtt_server.pub_device_location(topic, payload) #publish message
 return 

# posts location of asset - defines topic and payload for mqtt message
def post_location(asset):
    topic = "{}/{}/{}".format(asset.organisation, asset.id, "location") # topic unique to device
    #payload with device information
    payload = {"time": str(time.ctime),
               "org": asset.organisation,
               "name": asset.id,
               "type": asset.type,
               "lat": asset.location[0],
               "lon": asset.location[1],}
    mqtt_server.pub_device_location(topic, payload) # publish to MQTT Broker using topic and payload
    return 

# 1. first create dummies and publish their data for saving to DB
  # 2 next we retrieve location info for specific devices
def main():
  
  print("\n\n Creating dummy devices....")
  devices = create_dummies()    # create dummies
  print("   Publishing dummie devices .....")
  for device in devices:    # then publish these dummies to the server
     post_location(device)
  print("   Dummies PUBLISHED !!!")


  print("\n\n 2. Retrieve location_info for chosen device")
  company = input("    give organisation number: ") #give org.number in terminal
  device_id = input("   give device id: ") #give id in terminal
  get_location(company, device_id)

  mqtt_server.shut_down()   # shut down mqtt client

main()


  

 
  

