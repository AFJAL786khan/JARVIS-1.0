import cv2
import face_recognition

# Load the known faces and their names
known_faces = [
    ("Afzal Khan", "Data/photos/afzal.jpg"),
    ("Suleman Khan", "Papa1.jpg"),
    ("Salman Khan", "salman1.jpg"),
    ("Mr. Upendra Dutt Sharma", "Upendra_Sir.jpg")

    # Add more known faces with their respective images
]

# Load the known face images and encode them
known_face_encodings = []
known_face_names = []
for face_name, face_image in known_faces:
    image = face_recognition.load_image_file(face_image)
    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) > 0:
        face_encoding = face_encodings[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(face_name)
    else:
        print("No face found in image:", face_image)

# Open the camera
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()
    flipped_frame = cv2.flip(video_data, 1)
    gray_frame = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)

    face_locations = face_recognition.face_locations(flipped_frame)
    face_encodings = face_recognition.face_encodings(flipped_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Check if there's a match with known faces
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw rectangle and label on the face
        cv2.rectangle(flipped_frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(flipped_frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow('Face Recognition', flipped_frame)

    if cv2.waitKey(10) == ord('a'):
        break

video_cap.release()
cv2.destroyAllWindows()
