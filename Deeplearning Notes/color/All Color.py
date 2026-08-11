import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)

# Define color ranges in HSV
colors = {
    "Red": [(0, 120, 70), (10, 255, 255)],
    "Red 2": [(170, 120, 70), (180, 255, 255)],
    "Green": [(36, 100, 100), (86, 255, 255)],
    "Blue": [(94, 80, 2), (126, 255, 255)],
    "Yellow": [(15, 100, 100), (35, 255, 255)],
    "Orange": [(10, 100, 20), (25, 255, 255)],
    "Purple": [(129, 50, 70), (158, 255, 255)],
    "Pink": [(160, 50, 70), (170, 255, 255)],
    "White": [(0, 0, 200), (180, 30, 255)],
    "Black": [(0, 0, 0), (180, 255, 30)],
    "Gray": [(0, 0, 40), (180, 30, 200)],
    "Brown": [(10, 100, 20), (20, 255, 200)]
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, (lower, upper) in colors.items():
        lower = np.array(lower)
        upper = np.array(upper)

        # Create mask
        mask = cv2.inRange(hsv, lower, upper)

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > 500:  # filter noise
                x, y, w, h = cv2.boundingRect(cnt)

                # Draw rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Print color name
                cv2.putText(frame, color_name, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                            (0, 255, 0), 2)

    cv2.imshow("Color Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()




































