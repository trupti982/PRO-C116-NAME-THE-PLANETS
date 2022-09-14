import cv2

img=cv2.imread("C:/Users/shaur/OneDrive/Desktop/PRO-c116-OpenCV-Image-Assets-main/PRO-c116-OpenCV-Image-Assets-main/butterfly.jpg")
cv2.imshow("Display Image",img)
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Grayscale", gray_img)
cv2.waitKey(0)