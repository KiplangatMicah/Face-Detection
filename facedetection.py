
import cv2

# Load the cascade
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
camera = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = camera.read()
    # Convert to grayscale
    graycolor = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    face = cascade.detectMultiScale(gray, 1.1, 5)
    # Draw the rectangle around each face
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressedq
    key = cv2.waitKey(1) & 0xff
    if key==ord("q"):
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()