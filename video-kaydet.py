import cv2

cap = cv2.VideoCapture(0)

fileName = "kayit.avi"
codec = cv2.VideoWriter_fourcc('W','M','V','2')
frameRate = 30
resoulution = (640,480)

videoKaydet = cv2.VideoWriter(fileName, codec, frameRate, resoulution)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    videoKaydet.write(frame)

    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoKaydet.release()
cap.release()
cv2.destroyAllWindows()