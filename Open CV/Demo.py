import cv2

#1 represents colored image (3D matrix) whereas 0 represents grey image(2D Matrix)
img = cv2.imread
("C:\\Users\\pwayk\\Downloads\\ISEC_2021-10-12_09-46-50.png",1)
 
# resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
 
# print(img.shape)

# cv2.imshow("ISEC", img)
# cv2.waitKey(0) # 0 means it will wait till the user presses any key and uf a number is given it will consisere it as number of miliseconds .
# cv2.destroyAllWindows()

#CAPTURING VIDEO
video = cv2.VideoCapture(0) #0 means use built-in cam
a = 1
while True:
    a=a+1
    check, frame = video.read()
    print(frame)
    gray = cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("capture", gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break;
# import time
# time.sleep(3)
# #Capturing the first pic of the video
# #A video is basically set of images moving changing rapidly
# cv2.imshow("Capture",frame)
print(a)
video.release()
cv2.destroyAllWindows()


video.relese()
