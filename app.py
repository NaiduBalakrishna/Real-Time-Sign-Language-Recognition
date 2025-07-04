import cv2
from flask import Flask, Response, render_template, jsonify
from ultralytics import YOLO
import threading
import pyttsx3
import time

app = Flask(__name__)

# Load YOLO model
model = YOLO(r"C:\Users\balak\OneDrive\Desktop\sign-2\sign\best.pt")

# Initialize camera and text-to-speech engine
camera = None
camera_running = False
engine = pyttsx3.init()
engine.setProperty('rate', 120)  # Adjust speech rate
engine.setProperty('volume', 1.0)  # Set volume to max
last_spoken_time = time.time()  # Track last spoken time
speak_interval = 2  # Minimum interval between speech announcements
spoken_labels = set()  # Track spoken labels to avoid repetition

detected_signs = set()

def speak(text):
    """Function to convert text to speech with a delay between announcements."""
    global last_spoken_time
    current_time = time.time()
    
    if current_time - last_spoken_time > speak_interval:
        engine.say(text)
        engine.runAndWait()
        last_spoken_time = time.time()

def generate_frames():
    global camera, camera_running, spoken_labels, detected_signs
    while camera_running:
        success, frame = camera.read()
        if not success:
            break

        # Run YOLO detection
        results = model(frame)
        frame = results[0].plot()  # Draw bounding boxes
        
        # Extract detected text and speak it
        detected_texts = set()
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])  # Get class ID
                label = model.names[class_id]  # Convert to label
                detected_texts.add(label)
        
        # Update detected signs
        detected_signs = detected_texts

        # Speak new labels without blocking the stream
        new_labels = detected_texts - spoken_labels  # Avoid repeating the same labels
        if new_labels:
            spoken_labels.update(new_labels)
            threading.Thread(target=speak, args=(" ".join(new_labels),)).start()

        # Encode frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # Yield frame in MJPEG format
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    global camera, camera_running

    if not camera_running:
        return Response("Camera is not running", status=503)

    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_detected_signs')
def get_detected_signs():
    """Endpoint to get detected signs dynamically."""
    return jsonify(list(detected_signs))

@app.route('/start_camera', methods=['GET'])
def start_camera():
    global camera, camera_running
    if not camera_running:
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            return jsonify({"status": "error", "message": "Failed to access camera"}), 500
        camera_running = True
        return jsonify({"status": "started"})
    return jsonify({"status": "already running"})

@app.route('/stop_camera', methods=['GET'])
def stop_camera():
    global camera, camera_running
    if camera_running:
        camera_running = False
        if camera:
            camera.release()
        return jsonify({"status": "stopped"})
    return jsonify({"status": "already stopped"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
