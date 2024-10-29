import cv2
import os

# Global variables
ref_point = []
drawing = False
current_annotation = None
class_id = 0


def click_and_draw(event, x, y, flags, param):
    global ref_point, drawing, current_annotation

    # Start drawing the rectangle on left button down
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        drawing = True

    # Update the current rectangle while dragging the mouse
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        image_copy = image.copy()
        cv2.rectangle(image_copy, ref_point[0], (x, y), (0, 255, 0), 2)
        cv2.imshow("Image", image_copy)

    # Finalize the rectangle on left button release
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        drawing = False
        # Draw the final rectangle on the original image
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        # Calculate YOLO format values
        x_center = (ref_point[0][0] + ref_point[1][0]) / 2 / image.shape[1]
        y_center = (ref_point[0][1] + ref_point[1][1]) / 2 / image.shape[0]
        width = abs(ref_point[1][0] - ref_point[0][0]) / image.shape[1]
        height = abs(ref_point[1][1] - ref_point[0][1]) / image.shape[0]
        # Update current annotation
        current_annotation = f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"


def save_annotations(filename):
    with open(filename, 'w') as file:
        if current_annotation:
            file.write(current_annotation + "\n")
    print(f"Annotation saved to {filename}")


def load_annotations(filename):
    if not os.path.exists(filename):
        print("No saved annotations found.")
        return

    with open(filename, 'r') as file:
        annotation = file.readline().strip()
        # Parse annotation and draw the rectangle
        if annotation:
            global current_annotation
            current_annotation = annotation
            class_id, x_center, y_center, width, height = map(float, annotation.split())
            x_center *= image.shape[1]
            y_center *= image.shape[0]
            width *= image.shape[1]
            height *= image.shape[0]
            # Calculate top-left and bottom-right corners
            top_left = (int(x_center - width / 2), int(y_center - height / 2))
            bottom_right = (int(x_center + width / 2), int(y_center + height / 2))
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    print("Annotations loaded.")


def main():
    global image, current_annotation

    # Load image
    image_path = "./data/tomatoes.jpg"  # Replace with your image path
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return

    # Load saved annotations if they exist
    load_annotations("./labels/annotations.txt")

    clone = image.copy()
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", click_and_draw)

    while True:
        cv2.imshow("Image", image)
        key = cv2.waitKey(1) & 0xFF

        # Press 'r' to reset the image for new annotation
        if key == ord("r"):
            image = clone.copy()
            current_annotation = None

        # Press 's' to save annotations
        elif key == ord("s"):
            save_annotations("labels/annotations.txt")

        # Press 'q' to exit
        elif key == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
