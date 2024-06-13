import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("C:/Users/Jaliya Nimantha/OneDrive/Desktop/Mora 4t Sem/Projects/New folder/best.pt")

# Open a connection to the webcam (0 is the default camera, you might need to change this index if you have multiple cameras)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame reading was successful
    if ret:
        # Run YOLO model on the captured frame
        results = model(frame)

        # Iterate over the results and render them
        for result in results:
            annotated_frame = result.plot()

        # Display the resulting frame
        cv2.imshow('YOLO Detection', annotated_frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Could not read frame.")
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
