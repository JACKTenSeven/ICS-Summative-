from meross_iot.manager import MerossManager
from meross_iot.meross_event import MerossEventType
from meross_iot.cloud.devices.light_bulbs import GenericBulb
import time
import os


EMAIL = os.environ.get('Jack.maxwell0360@gmail.com') or "Jack.maxwell0360@gmail.com"
PASSWORD = os.environ.get('Jack143b') or "Jack143b"

def event_handler(eventobj):
    if eventobj.event_type == MerossEventType.DEVICE_ONLINE_STATUS:
        print("Device online status changed: %s went %s" % (eventobj.device.name, eventobj.status))
        pass
    elif eventobj.event_type == MerossEventType.DEVICE_SWITCH_STATUS:
        print("Switch state changed: Device %s (channel %d) went %s" % (eventobj.device.name, eventobj.channel_id,
                                                                        eventobj.switch_state))
    else:
        print("Unknown event!")



if __name__=='__main__':
    manager = MerossManager(meross_email=EMAIL, meross_password=PASSWORD)
    manager.register_event_handler(event_handler)
    manager.start()
    b_device = manager.get_device_by_name("B")
    a_device = manager.get_device_by_name("A")
   
    
    
    rvalue = 255
    gvalue = 255
    bvalue = 255

    
    b_device.set_light_color(rgb=(255, 255, 255))
    a_device.set_light_color(rgb=(rvalue, gvalue, bvalue), luminance =5)
       
            
            
            
   
