import cv2

cam = cv2.VideoCapture(0)
count = 0
cam.set(3, 640)
cam.set(4, 480)

imgBackground2 = cv2.imread('Resources/background2.png')

while True:
    success, img = cam.read()

    k = cv2.waitKey(1)
    imgBackground2[162:162+480, 60:60+640] = img
    # cv2.imshow("Test",img)
    cv2.imshow("Image Capturing System", imgBackground2)
    if k%256 == 27:
        print("Images Captured Successfully ")
        break
    elif k%256 == 32:
        print("Image "+str(count)+" saved")
        file = 'C:/Users/Lokesh T/PycharmProject/face/Capture/img'+str(count)+'.png'
        cv2.imwrite(file, img)
        count += 1
