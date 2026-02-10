
# Real-Time Allen Screw Detector & Distance Estimator

This project implements a real-time computer vision system capable of detecting "Allen screws" and estimating their distance (Z-depth) from the camera. It utilizes a custom-trained **YOLOv8** model for object detection and the **Triangle Similarity Principle** for depth estimation.

## Demos
[yolov8x.webm](https://github.com/user-attachments/assets/4631a0d2-50bc-40ed-a235-7558f37b55a9)


## Key Features

* **Real-Time Detection:** Uses Ultralytics YOLOv8 for fast and accurate inference via webcam.
* **Distance Estimation:** Calculates the Z-axis depth (in cm) based on the object's pixel width.
* **Robot-Ready Output:** Prints coordinates (X, Y, Z) to the console for integration with robotic arms or pick-and-place systems.
* **High Accuracy Model:** Trained on a custom dataset with exceptional precision for screw classes.

---

##  Model Performance

The model was trained for 50 epochs and achieved high performance metrics, ensuring reliable detection in deployment.

* **Architecture:** YOLOv8 (Nano) with ~3 million parameters.
* **Final Precision:** 95.7%.
* **Final Recall:** 85.3%.
* **mAP50-95 (Mean Average Precision):** 0.839.

### Class-Specific Performance
The model is specifically optimized for the target class used in the script:
* **Allen Screw:** 98.9% mAP @ 50 IoU.
* **Screw:** 92.6% mAP @ 50 IoU.

---

##  Prerequisites

* Python 3.8+
* A webcam (connected to index `0` by default).
* A known physical measurement of your target object (width of the bolt head).

### Dependencies
Install the required libraries:
```bash
pip install opencv-python numpy ultralytics

```

---

##  Configuration & Calibration

Before running `run.py`, must configure the constants at the top of the file to match your hardware setup.

### 1. Set Physical Dimensions

Open `run.py` and modify `REAL_WIDTH`:

```python
# Actual width of the bolt head (in cm or mm)
# If using cm, your distance output will be in cm.
REAL_WIDTH = 1.0  

```

### 2. Calibrate Focal Length

The script uses a hardcoded `FOCAL_LENGTH = 800`. To get accurate distance readings, you must calculate the specific focal length for your camera:

1. Place the Allen screw at a **known distance** (e.g., 20 cm) from the camera.
2. Run a temporary script or print the `pixel_width` detected by YOLO.
3. Apply the formula:
<img width="147" height="74" alt="image" src="https://github.com/user-attachments/assets/c691ad96-7681-4923-9a21-2ac456387edf" />

*  Apparent width in pixels (from the camera).
*  Actual distance (e.g., 20 cm).
*  Real width of the object (e.g., 1.0 cm).


4. Update the value in `run.py`:
```python
FOCAL_LENGTH = 800 # Replace with calculated value

```



---

##  Usage

1. Ensure your trained model weights (`best.pt`) are in the same directory as the script.
2. Run the script:
```bash
python run.py

```


3. **Visual Output:** A window will open showing the bounding box, class name, and calculated distance.
4. **Data Output:** The console will stream coordinate data:
```text
Found Allen screw at X:320 Y:240 Z:15.42
Found Allen screw at X:325 Y:238 Z:15.38

```


5. Press **'q'** to quit the application.

---

## Logic Explanation

The distance calculation relys on the relationship between focal length (), real object width (), and observed pixel width ():

1. **Detection:** YOLOv8 finds the object and returns a bounding box.
2. **Pixel Width:** The script calculates the width of the box in pixels ().
3. **Depth Calculation:**
$$ Distance = \frac{W \times F}{P} $$
This formula is derived from the triangle similarity principle, assuming the object is facing the camera directly.

---

##  Project Structure

```text
.
├── run.py          # Main inference and distance estimation script
├── best.pt         # Trained YOLOv8 model weights (required)
├── README.md       # Project documentation
└── output.md       # (Optional) Training logs and metrics

```

## ⚠️ Troubleshooting

* **Camera not opening:** Change `cv2.VideoCapture(0)` to `1` or `2` if you have multiple cameras.
* **Inaccurate Distance:** Ensure `REAL_WIDTH` is precise and re-calculate `FOCAL_LENGTH`. Lighting conditions can vary the detected pixel width.
* **Model not found:** Ensure `MODEL_PATH = 'best.pt'` points to the correct file location.
