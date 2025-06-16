# import os

# if(not os.path.exists("data")):
#     os.mkdir("data") #creates directory or folder

# for i in range (0,100):
#     os.mkdir(f"data/Day{i+1}") #creates folders inside folder

import os

for i in range (0,100):
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1} ")  

SKIPPED AFTER THAT