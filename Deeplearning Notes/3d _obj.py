# -------------------- IMPORT LIBRARIES --------------------
import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
import urllib.request

# -------------------- MEDIAPIPE SETUP --------------------
mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

# -------------------- FUNCTION: LOAD IMAGE FROM URL --------------------
def url_to_array(url):
    headers = {"User-Agent": "Mozilla/5.0"}  # Fix for 403 error
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)

    arr = np.asarray(bytearray(resp.read()), dtype=np.uint8)  # correct dtype
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img

# -------------------- IMAGE URL --------------------
image_url = "https://upload.wikimedia.org/wikipedia/commons/4/4b/Coffee_break_%283457656569%29.jpg"
image = url_to_array(image_url)

# -------------------- OBJECTRON MODEL --------------------
objectron = mp_objectron.Objectron(
    static_image_mode=True,
    max_num_objects=5,
    min_detection_confidence=0.2,
    model_name='Cup'
)

# -------------------- PROCESS IMAGE --------------------
results = objectron.process(image)

# -------------------- DRAW RESULTS --------------------
annotated_image = image.copy()

if not results.detected_objects:
    print("No objects detected.")
else:
    for obj in results.detected_objects:
        # Draw 2D box
        mp_drawing.draw_landmarks(
            annotated_image,
            obj.landmarks_2d,
            mp_objectron.BOX_CONNECTIONS
        )

        # Draw 3D axis
        mp_drawing.draw_axis(
            annotated_image,
            obj.rotation,
            obj.translation
        )

# -------------------- DISPLAY OUTPUT --------------------
plt.figure(figsize=(10, 10))
plt.imshow(annotated_image)
plt.axis('off')
plt.title("3D Object Detection (Cup)")
plt.show()