#wap to clear the clutter inside 
#a folder on your computer.
#You should use os module to 
# rename all the png images from 
# 1.png all the way till n.pnd where
#  n is the number of png files in 
# that folder. Do the same for 
# other file formats

import os

files= os.listdir("cluttered folder")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"cluttered folder/{file}",f"cluttered folder/{i}.png")
    i=i+1
