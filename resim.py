import cv2 

img_color = cv2.imread("cedric.jpg")
img_gray = cv2.imread("cedric.jpg",0)

cv2.namedWindow("Cedric Color",cv2.WINDOW_NORMAL)  #resmi boyutlandırma.

cv2.imshow("Cedric Color",img_color)
cv2.imshow("Cedric Gray",img_gray)

cv2.imwrite("cedric3.jpg", img_color) #resmi kaydetme

cv2.waitKey(0)
cv2.destroyAllWindows() 