#pip install opencv-python numpy

import cv2
import math
from ultralytics import YOLO

# --- CONFIGURATION ---
MODEL_PATH = 'best.pt'   # Path to your trained model
REAL_WIDTH = 1.0         # Actual width of the bolt head (in cm or mm)
FOCAL_LENGTH = 800       # The 'F' value you calculated in Phase 2
TARGET_CLASS = 'Allen screw' # The class name you want to find

# Load the model
model = YOLO(MODEL_PATH)

# Start Webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

def calculate_distance(focal_length, real_width, pixel_width):
    if pixel_width == 0: return 0
    return (real_width * focal_length) / pixel_width

while True:
    success, frame = cap.read()
    if not success:
        break

    # Run YOLO inference
    results = model(frame, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Check if detection is our target class
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            
            if cls_name == TARGET_CLASS:
                # Get Bounding Box Coordinates
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # 1. Calculate Center (X, Y)
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)

                # 2. Calculate Width in Pixels
                pixel_width = x2 - x1

                # 3. Calculate Depth (Z)
                depth = calculate_distance(FOCAL_LENGTH, REAL_WIDTH, pixel_width)

                # Draw Visuals
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
                
                label = f"{cls_name} Z:{depth:.2f}cm Center:({center_x},{center_y})"
                cv2.putText(frame, label, (x1, y1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                # Output to console (for robot/process)
                print(f"Found {cls_name} at X:{center_x} Y:{center_y} Z:{depth:.2f}")

    cv2.imshow("Bolt classifierS", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()