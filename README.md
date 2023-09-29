# Image_Denoiser
Welcome to the "Image Denoiser" project, a web application designed to enhance the quality of your images by reducing noise and imperfections. This project leverages the power of Flask, a lightweight Python web framework, and OpenCV, an open-source computer vision library, to offer a user-friendly and accessible platform for image processing.

Whether you're a photographer looking to enhance the quality of your photos or just want to clean up some images, Image Denoiser provides a user-friendly platform for this purpose.
## Table of Contents
- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Key Features
1. Image Denoising: Upload images and fine-tune the denoising level to achieve the desired result.
2. Easy-to-Use Interface: The intuitive web interface ensures a seamless user experience.
3. Fast Processing: Leveraging the capabilities of OpenCV, your images are processed quickly and efficiently.
4. Dynamic Feedback: See the immediate impact of the denoising process with real-time previews.
5. Image Preservation: Tailor the denoising level to maintain essential details while reducing noise.
Whether you're a photography enthusiast looking to enhance your images or a professional seeking to improve the quality of visuals, Image Denoiser simplifies the process, delivering exceptional results in moments.

## Prerequisites
Before you begin using Image Denoiser, ensure that you have the following prerequisites in place:

1. Python (>= 3.6): Image Denoiser is built with Python, so you need a Python installation.
2. Flask: Image Denoiser relies on the Flask web framework.
3. OpenCV: Image Denoiser uses OpenCV for image processing.
4. NumPy: NumPy is used for numerical operations in the project.
With these prerequisites in place, you'll be ready to run Image Denoiser and enhance your images quickly and effectively.

## Getting started
Follow these steps to quickly get started with Image Denoiser and enhance the quality of your images:
1. Clone the Repository: Begin by cloning the Image Denoiser repository to your local machine. Open your terminal or command prompt and use the following command:
```
git clone https://github.com/RohanBiswas67/Image_Denoiser
cd Image_Denoiser
```
2. Install Python: If you don't already have Python installed, [download](https://www.python.org/downloads/) and install it from the official Python website. Image Denoiser requires Python 3.6 or higher.
   
>Linux Users can do it directly using system's package manager (e.g., apt for Ubuntu):
  ```
  sudo apt update
  sudo apt install python3
  ```
>For MacOS users , You can install Python 3 using Homebrew, a popular package manager for macOS:
  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  brew install python
  ```
4. Install Dependencies: Image Denoiser relies on a few Python packages. You can install these dependencies using pip, the Python package manager. Run the following commands to install Flask, OpenCV, and NumPy:
```
pip install Flask
pip install opencv-python
pip install numpy
```
Run the Application: Once the dependencies are installed, you can start the Image Denoiser web application. Use the following command:
```
python app.py
```
This command will start the Flask development server.

Now, you're ready to enhance your images with Image Denoiser. Enjoy the benefits of cleaner and crisper visuals!

## Usage 
Image Denoiser simplifies the process of enhancing the quality of your images by reducing noise and imperfections. Follow these steps to use the application effectively:
1. Access the Web Application: Open your web browser and navigate to http://localhost:5000. The main page of the Image Denoiser web application will load.
2. Upload an Image:
  - Click on the file input box to select an image file from your computer. Supported image formats include JPEG, PNG, and more.
3. Adjust the Denoising Level:
  Below the image preview, you'll find an input field labeled "Denoising Level (0-100)." You can adjust the denoising level by entering a value between 0 and 100.

  - A lower value (e.g., 0) means minimal denoising,
  - A higher value (e.g., 100) represents strong denoising.
4. Apply Denoising:
  - After selecting an image and setting the denoising level, click the "Upload and Denoise" button. The denoising process will begin.
5. View the Denoised Image:
  - Once the denoising is complete, the denoised image will be displayed below the input form.
You can compare the original and denoised images to observe the improvement.
Repeat as Needed:
+ If you're not satisfied with the results, you can adjust the denoising level and click "Upload and Denoise" again to see the effect of different settings.
Download the Denoised Image
+ If you're satisfied with the denoised image, you can right-click on the denoised image and choose "Save image as" to save it to your computer.

## Contributing
Contributions are welcome! If you would like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```
   git commit -m 'Add new feature'
   ```
4. Push to the branch:
   ```
   git push origin feature-name
   ```
5. Submit a pull request.

## License
This project is licensed under the [MIT License](https://github.com/RohanBiswas67/Image_Denoiser/blob/main/LICENSE).
