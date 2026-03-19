from flask import Flask, render_template, request
import base64
import cv2
import numpy as np

app = Flask(__name__)

def analyze_skin(img):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return "No face detected. Try again."

    return "Face detected! Skin looks healthy. Use sunscreen daily."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.form['image']

        image_data = data.split(',')[1]
        nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (300, 300))
        result = analyze_skin(img)

        return render_template('result.html', result=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run()