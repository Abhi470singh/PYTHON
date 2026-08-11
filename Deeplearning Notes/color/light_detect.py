import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.set_page_config(page_title="Light Detection", page_icon="💡")
st.title("💡 Room Light Detection using Webcam")

# Sidebar slider to adjust threshold
threshold = st.sidebar.slider("Brightness Threshold", 0, 255, 100)

class LightDetector(VideoTransformerBase):
    def __init__(self):
        self.threshold = threshold

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Calculate average brightness
        brightness = np.mean(gray)
        
        # Detect ON/OFF
        if brightness > self.threshold:
            text = f"Light: ON ({int(brightness)})"
            color = (0, 255, 0)
        else:
            text = f"Light: OFF ({int(brightness)})"
            color = (0, 0, 255)
        
        # Overlay on frame
        cv2.putText(img, text, (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
        
        return img

# Start webcam
webrtc_streamer(
    key="light-detector",
    video_transformer_factory=LightDetector
)
