import psutil 
from notifypy import Notify

ShowBattery= psutil.sensors_battery()
if ShowBattery[0] == 100 and ShowBattery[2]== True:
    notification = Notify()
    notification.title = "Battery Full💯"
    notification.message = "Unplug the Charger. "
    notification.send()
else:
    if ShowBattery[0]== 25 and ShowBattery[2]== False:
        notification = Notify()
        notification.title = "Battery Low😒"
        notification.message = "Plug In the Charger. "
        notification.send()
        print("plug in ")    

print(ShowBattery[0])




