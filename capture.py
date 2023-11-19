import cv2
import time
from PIL import Image
import numpy as np
import os

# Folder
folder = "frames"

# Create the frames folder if it doesn't exist
frames_dir = os.path.join(os.getcwd(), folder)
os.makedirs(frames_dir, exist_ok=True)

# Initialize the video capture
cap = cv2.VideoCapture("videos/clippers.mp4")

# Wait for the camera to initialize and adjust light levels
time.sleep(2)

while True:
    ret, frame = cap.read()
    if ret:
        # Convert the frame to a PIL image
        pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Convert the PIL image back to an OpenCV image
        frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

        # Display the frame
        cv2.imshow("Video Preview", frame)

        # Save the frame as an image file
        print("Saved current frame")
        path = f"{folder}/frame.jpg"
        cv2.imwrite(path, frame)
    else:
        print("Failed to capture image")
        break

    # Check if the user pressed the 'q' key
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
