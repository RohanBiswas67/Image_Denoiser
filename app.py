import os
from flask import Flask, render_template, request, send_from_directory
import cv2
import numpy as np

app = Flask(__name__, static_url_path='/static')


UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

# Function to denoise the image
def denoise_image(image, denoising_level):
    """
    Denoise the input image based on the specified denoising level.

    :param image: Input image to denoise.
    :param denoising_level: Level of denoising to apply.
    :return: Denoised image.
    """
    if denoising_level == 0:
        return image
    elif denoising_level == 100:
        return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    else:
        return cv2.fastNlMeansDenoisingColored(image, None, denoising_level, 10, 7, 21)

@app.route('/')
def index():
    """
    Render the main page.
    :return: Rendered HTML template for the main page.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    """
    Handle image upload and denoising.

    :return: HTML response with the denoised image or an error message.
    """
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        denoising_level = int(request.form.get('denoising_level', 0))
        image = cv2.imread(image_path)
        denoised_image = denoise_image(image, denoising_level)

        result_path = os.path.join(app.config['RESULT_FOLDER'], file.filename)
        cv2.imwrite(result_path, denoised_image)

        return f'<img src="{result_path}" alt="Denoised Image">'
    return "Error"

@app.route('/results/<filename>')
def uploaded_file(filename):
    """
    Serve the denoised image from the results folder.

    :param filename: Name of the denoised image file.
    :return: Denoised image file.
    """
    return send_from_directory(app.config['RESULT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
