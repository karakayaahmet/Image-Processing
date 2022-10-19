import cv2
from cv2 import flip

cap = cv2.VideoCapture(0) #webcamden görüntü alınmakta.

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()