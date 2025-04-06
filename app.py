from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
SKETCH_FOLDER = 'sketches'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SKETCH_FOLDER, exist_ok=True)

def convert_to_sketch(image_path):
    img = cv2.imread(image_path)

    # Resize to 1080p while keeping aspect ratio
    height, width = img.shape[:2]
    target_height = 1080
    scale_ratio = target_height / float(height)
    new_width = int(width * scale_ratio)
    resized_img = cv2.resize(img, (new_width, target_height), interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    # Invert image
    inv = 255 - gray

    # Apply Gaussian blur for softness
    blur = cv2.GaussianBlur(inv, (15, 15), 0)

    # Blend for sketch effect
    sketch = cv2.divide(gray, 255 - blur, scale=256)

    # Optional: Slightly sharpen the result
    kernel = np.array([[0, -1, 0],
                       [-1,  5, -1],
                       [0, -1, 0]])
    sketch = cv2.filter2D(sketch, -1, kernel)

    # Save result
    sketch_path = os.path.join(SKETCH_FOLDER, 'sketch.png')
    cv2.imwrite(sketch_path, sketch)
    return sketch_path

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        img_file = request.files['image']
        if img_file:
            filename = secure_filename(img_file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            img_file.save(filepath)

            sketch_path = convert_to_sketch(filepath)
            return send_file(sketch_path, as_attachment=True, download_name="sketch.png")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
