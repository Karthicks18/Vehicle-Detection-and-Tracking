#!/usr/bin/env python
# coding: utf-8

# # Vehicle Detection and Tracking

# In[4]:


import cv2
import imutils
file = "cars.xml"
c_file = cv2.CascadeClassifier(file)
cam = cv2.VideoCapture(0)
while True:
    _,img = cam.read()
    img = imutils.resize(img,width=1000)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars = c_file.detectMultiScale(gray,1.1,4)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
    cv2.imshow("Frame",img)
    
    b = str(len(cars))
    a = int(b)
    n = a
    print("---------------------------------------------------")
    print("North: %d " %(n))
    if n>=8:
        print("North more traffic, Turn to RED")
    else:
        print("No traffic")
    if cv2.waitKey(30) == 27:
        break
    
cam.release()
cv2.destroyAllWindows()


# In[ ]:




