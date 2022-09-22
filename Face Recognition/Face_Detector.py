import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
#img = cv2.imread('willsmith.png')
#img = cv2.imread('couple2.png')

# To capture video from webcam
webcam = cv2.VideoCapture(0)

# To capture from video
#webcam = cv2.VideoCapture('peoplevideo.mp4')

# Iterate forever over frames
while True:

    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 256, 0), 10)

    cv2.imshow('KW Face Detector', frame)
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key==81 or key==113:
        break

# Release the VideoCapture object
webcam.release()

print("Code Completed")












"""
# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Face coordinates example: [[51 260 566 566]] (First 2 sets of number would be (x) and (y) coordinates, Second 2 sets of numbers would be width and height
    #print(face_coordinates)

# Draw rectangles around the faces
    #(x, y, w, h) = face_coordinates[0]
    #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 10)

# Above code works so now create a "for loop" to keep cycling through the image to detect multiple faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 256, 0), 10)

# Display the image with the faces
cv2.imshow('KW Face Detector', img)
cv2.waitKey()

print("Code Completed")
"""