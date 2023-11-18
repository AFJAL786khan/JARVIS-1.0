import cv2

# contains pre-trained classifiers for detecting frontal faces.
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
# Capture Video using camera
video_cap = cv2.VideoCapture(0)

while True:
    
    ret, video_data = video_cap.read()
    # Flipped camera
    flipped_frame = cv2.flip(video_data, 1)
    
    # Changed Color of the video capture to grey so System can understand and detect
    gray_frame = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)
    
    # Style The green rectangle that hovers on the face
    faces = face_cap.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Setting height, width, and X-axix and Y-axis of the green frame
    for (x, y, w, h) in faces:
        cv2.rectangle(flipped_frame, (x, y), (x + w, y + h), (0, 255, 2), 2)
        
        # Name of the Camera window
    cv2.imshow('Face Recognition', flipped_frame)
    
    # If we press 'a' the program will be terminated
    if cv2.waitKey(10) == ord('a'):
        break

video_cap.release()
cv2.destroyAllWindows()
