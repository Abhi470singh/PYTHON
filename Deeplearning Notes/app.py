import cv2
import mediapipe as mp
import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Face Transform App")

st.title("📸 Face Transform App (Webcam + Upload)")

# Initialize MediaPipe
mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection()

# Upload image
uploaded_file = st.file_uploader("Upload target face image", type=["jpg", "png", "jpeg"])

target_img = None

if uploaded_file:
    target_img = Image.open(uploaded_file)
    target_img = np.array(target_img)
    st.image(target_img, caption="Uploaded Image")

# Start webcam
run = st.checkbox("Start Webcam")

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

def detect_face(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = face_detection.process(rgb)
    if result.detections:
        det = result.detections[0]
        bbox = det.location_data.relative_bounding_box
        h, w, _ = img.shape
        x, y = int(bbox.xmin * w), int(bbox.ymin * h)
        w_box, h_box = int(bbox.width * w), int(bbox.height * h)
        return x, y, w_box, h_box
    return None

def overlay_face(frame, target):
    face1 = detect_face(frame)
    face2 = detect_face(target)

    if face1 and face2:
        x1, y1, w1, h1 = face1
        x2, y2, w2, h2 = face2

        face_target = target[y2:y2+h2, x2:x2+w2]
        face_target = cv2.resize(face_target, (w1, h1))

        # Blend
        frame[y1:y1+h1, x1:x1+w1] = cv2.addWeighted(
            frame[y1:y1+h1, x1:x1+w1], 0.3,
            face_target, 0.7, 0
        )

    return frame

if run:
    while True:
        ret, frame = cap.read()
        if not ret:
            st.write("Camera not working")
            break

        if target_img is not None:
            frame = overlay_face(frame, target_img)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

        # Stop condition
        if not run:
            break

cap.release()