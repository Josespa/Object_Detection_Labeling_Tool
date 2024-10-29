# Object Detection Labeling Tool

A simple Python tool for annotating bounding boxes in images for object detection. This tool uses OpenCV to allow users to manually draw a single bounding box on an image, save annotations, and reload them in YOLO format.

## Features

1. **Draw Bounding Box**: Allows real-time drawing of a rectangle on the image to mark an object.
2. **One Bounding Box at a Time**: Only one rectangle is allowed at a time. Drawing a new box replaces the previous one.
3. **Save and Load Annotations**: Annotations are saved in YOLO format and can be reloaded for further editing.

## Requirements

- Python 3.12.2
- OpenCV 4.10

Install OpenCV with:
```bash
pip install opencv-python
```
 
## Usage
Download the Code: Clone or download the code files to your local machine.

Place Your Image: Ensure your image file is in the same directory as the code, or provide the correct path.

Run the Tool:
```bash
python main.py
```

### Controls:

Draw Bounding Box: Click and drag the left mouse button on the image to draw a rectangle around the object.
- r: Reset the current annotation (removes the existing rectangle).
- s: Save the current annotation in annotations.txt in YOLO format.
- q: Quit the tool without saving additional changes.

### Notes
Only the last drawn bounding box is saved at any time.
The tool is intended for annotating a single object per image, suitable for YOLO-based object detection models.
