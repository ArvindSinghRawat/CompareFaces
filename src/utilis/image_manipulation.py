""" Utilities of Image Manipulation
"""
import os
import cv2

def resize_image(input_img, width: int, height: int):
    """Uses OpenCV's resize function to resize the input image in specific dimensions

    Args:
        input_img (OpenCV Image): Input Image
        width (int): Target size of the Image
        height (int): Target size of the Image
    """
    target_dimensions = (width, height)
    return cv2.resize(input_img, target_dimensions, interpolation=cv2.INTER_AREA)

if __name__ == "__main__":
    input_path = input("Enter name of the Image: ")
    PROJECT_PATH = ""
    IMAGE_SOURCE_PATH = os.path.join(PROJECT_PATH, "data/processed/images")
    IMAGE_PATH = os.path.join(IMAGE_SOURCE_PATH, input_path)
    img = cv2.imread(IMAGE_PATH, cv2.IMREAD_UNCHANGED)
    resized_image = resize_image(img, 96, 96)

    cv2.imshow("Resized image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
