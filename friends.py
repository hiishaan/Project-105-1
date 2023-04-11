import os
import cv2

path = "Images"
images = []

for file in os.listdir(path):
     name, ext = os.path.splitext(file)

     if ext == '.jpg':
          fullfilename = path+'/'+file
          images.append(fullfilename)

count = len(images)

sizetest = cv2.imread(images[0])
height, width, channels = sizetest.shape
size = (width, height)
print(size)

videotemp = cv2.VideoWriter('Friends Forever.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 0.75, size)

for i in range(0, count, 1):
     frame = cv2.imread(images[i])
     resizedFrame = cv2.resize(frame, size)
     videotemp.write(resizedFrame)

videotemp.release()
print("Done")
