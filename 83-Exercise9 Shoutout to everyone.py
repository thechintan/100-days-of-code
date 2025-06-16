# wap to pronounce list names using win32 API.
# if you are given list as follows:
# l=['rahul','nishant','chintan']

# your program should pronounce:
# shoutout to rahul
# shoutout to chintan
# shoutout to nishant

# #pip install pywin32
# import win32com.client

# # Initialize the SAPI.SpVoice COM object
# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# for voice in speaker.GetVoices():
#     print(voice.GetDescription())
# # Set the second available voice
# speaker.Voice = speaker.GetVoices().Item(1)

# # Speak the text
# speaker.Speak("Hello! I am speaking using Windows SAPI through Python.")



import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

list=["Chintan","Ram","Shyam","Ghanshyam"]
for i in list:
    speaker.speak(f"shoutout to{i}")

    #     message=f"Shoutout to {i}"
    # print(message)
    # speaker.speak(message)