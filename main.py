import cv2

# 1. Initialize the webcam (0 is usually the default built-in camera)
cap = cv2.VideoCapture(0)

# Check if the webcam opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # 2. Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break

    # 3. Display the resulting frame in a window named 'Webcam Feed'
    cv2.imshow('Webcam Feed', frame)

    # 4. Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Release the camera resource and close all active windows
cap.release()
cv2.destroyAllWindows()
