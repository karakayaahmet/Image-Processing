import cv2

img = cv2.imread("cedric.jpg")

img = cv2.resize(img,(640,720))

cv2.imshow("Image Color", img)

cv2.waitKey(0)

cv2.destroyAllWindows()