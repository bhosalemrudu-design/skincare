from flask import Flask, render_template, request
import cv2
import numpy as np

app = Flask(__name__)

# Dummy AI function (replace with real model)
def analyze_skin(image_path):
    # Simulated result
    return "Oily Skin with Acne"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']
    filepath = "static/" + file.filename
    file.save(filepath)

    result = analyze_skin(filepath)
    return render_template('result.html', result=result, image=filepath)

if __name__ == '__main__':
    app.run(debug=True)