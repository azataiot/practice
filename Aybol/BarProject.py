#library-------------------------------------------------------—
from matplotlib import pyplot
import numpy as np
import cv2
from datetime import datetime
#output time
time_save =datetime.now()
time_now = str(time_save.year)+"-"+str(time_save.month)+"-" + str(time_save.day)+"_"+ str(time_save.hour) + "." + str(time_save.minute) + "." + str(time_save.second)
#create diagramm--------------------------------------------------—
#
country = ['China', 'Russia', 'USA', 'Kazakhstan','Other countries']
visitors = []
i = 0
while(i < len(country)):
    try:
        print("How many pepople visit your site of {}".format(country[i]))
        vis = float(input())
        visitors.append(vis)
        i+=1
    except Exception:
        print("Error, u did'n insert number")

pyplot.barh(['C', 'U', 'R', 'K','OC'],visitors)
pyplot.title('{}'.format(time_now))
#save diagramm---------------------------------------------------—
pyplot.savefig("path\\plot{0}.jpg".format(time_now))

#function,which inserts image on image------------------------------—
def imageOnImage(largeImg , smallImg,x_offset, y_offset ):
    y1, y2 = y_offset, y_offset + smallImg.shape[0]
    x1, x2 = x_offset, x_offset + smallImg.shape[1]

    alpha_s =1
    print(alpha_s)
    alpha_l = 0

    for c in range(0, 3):
        largeImg[y1:y2, x1:x2, c] = (alpha_s * smallImg[:, :, c] + alpha_l * largeImg[y1:y2, x1:x2, c])

#create window size------------------------------------------------------—
height = 480
width = 640
#create layer or void image------------------------------------------------—
layer = np.zeros((height,width,3))
background = layer[:]
cv2.imwrite("path", background)

#call saved diagram-----------------------------------------------------—
background =cv2.imread("path")
img =cv2.imread("path\\plot{0}.jpg".format(time_now))


#change size diagram------------------------------------------------------—
reImg = cv2.resize(img,(height,width),cv2.INTER_AREA)

#backroung on void image--------------------------------------------------—
imageOnImage(background,reImg,0,0)

#call FlagImage-------------------------------------------------------------------------—
s1 = cv2.resize(cv2.imread("path"), (77, 50))
s2 = cv2.resize(cv2.imread("path"), (77, 50))
s3 = cv2.resize(cv2.imread("path"), (77, 50))
s4 = cv2.resize(cv2.imread("path"), (77, 50))
s0 = cv2.resize(cv2.imread("path"), (77, 50))

#Create array Image------------------------------------------------------------------------—
array = [s0,s1,s2,s3,s4]
dst = 75
for i in range(0,len(array)):
    imageOnImage(background,array[i],2,dst)
    dst+=70
cv2.imshow("hi",reImg)
cv2.waitKey(0)
cv2.destroyAllWindows()