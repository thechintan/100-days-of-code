# from plyer import notification
# import time

# Time= int(time.strftime("%H"))
# print(Time)

# if Time==8 and Time==9 and Time==23 :
#     # for i in range (16):
#     notification.notify(title ='Please drink water',app_name="Drink Water Reminder" ,message="It's H2O time.")
    
# else:
#     notification.notify(message="It's sleeping time")

# from plyer import notification
# import time

# if __name__=="__main__":
#     while True:
#         notification.notify(title ='Please drink water',app_name="Drinking water" ,message='Please drink water for your own safety',timeout=0.5 )
#         time.sleep(3600)

import time
from plyer import notification

# Function to show the notification
def remind_to_drink_water():
    notification.notify(
        title='💧 Water Reminder!',
        message='Time to drink a glass of water 🚰',
        timeout=5  # seconds
    )

# Reminder every 1 hour (adjust as needed)
# interval = 10  # 1 hour in seconds

# Run reminder for 8 times (8 hours)
for i in range(6):
    remind_to_drink_water()
    time.sleep(10)
