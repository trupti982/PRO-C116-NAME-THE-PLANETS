import cv2
img=cv2.imread("C:/Users/shaur/OneDrive/Desktop/PRO-c116-OpenCV-Image-Assets-main/PRO-c116-OpenCV-Image-Assets-main/poster.jpg")
rocket = img[120:360,400:500]
img[0:240, 500:600] = rocket
text_to_show = "I love coding at WhiteHatJr."
cv2.putText(img, text_to_show, (20, 220), 
fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
fontScale=1, color=(0,0,255) )
cv2.imshow("output",img)
cv2.waitKey(0)