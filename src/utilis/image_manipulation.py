""" Utilities of Image Manipulation
"""
import os
import cv2


def create_nested_directories(parent_path: str, dir_name_list: list) -> str:
    """Create a series of Nested directories inside the parent_path

    Args:
        parent_path (str): Directory where generated directories
        will be created
        dir_name_list (list): List of directorie names where each
        directory is created inside another

    Returns:
        str: Path to innermost created directory
    """
    copy = parent_path + ""
    for dir_name in dir_name_list:
        if not create_directory(copy, dir_name):
            break
        copy = os.path.join(copy, dir_name)
    return copy


def create_directory(
        parent_path: str, dir_name: str, verbosity: bool = False) -> bool:
    """Creates a "dir_name" directory in "parent_path" directory,
    suppresses  FileExistsError and,
    return True, if required directory is generated/exists,
    otherwise return False

    Args:
        parent_path (str): Path to Target Directory,
        where new directory is needed to be created
        dir_name (str): Name of new directory
        verbosity (bool, optional): Prints error if Found, Defaults to False.

    Returns:
        bool: Returns True, if desired directory is created/exists,
        otherwise False
    """
    try:
        os.mkdir(os.path.join(parent_path, dir_name), mode=0o771)
    except FileExistsError:
        pass
    except FileNotFoundError:
        if verbosity:
            print("Target directory does not exist")
        return False
    return True


def resize_image(input_img, width: int, height: int):
    """Uses OpenCV's resize function to resize the input image in specific dimensions

    Args:
        input_img (OpenCV Image): Input Image
        width (int): Target size of the Image
        height (int): Target size of the Image
    """
    target_dimensions = (width, height)
    return cv2.resize(input_img, target_dimensions, interpolation=cv2.INTER_AREA)


def resize_and_export(input_path: str, target_path: str, width: int, height: int):
    """Resize all the images in the input_path directory and export them to target_path

    Args:
        input_path (str): Path for the Image source directory
        target_path (str): Path for the target directory where exported image will be saved
        width (int): Target size of the Image
        height (int): Target size of the Image
    """

    print(input_path)

    for image_name in os.listdir(input_path):
        input_path = os.path.join(input_path, image_name)
        export_path = create_nested_directories(
            target_path, ["Resized_Images", image_name])
        print(export_path)
        try:
            image = cv2.imread(input_path)

            resized_image = resize_image(image, width, height)

            result_filename = os.path.join(export_path, "resized.jpg")

            print(cv2.imwrite(result_filename, resized_image))
        except:
            pass


if __name__ == "__main__":
    image_name = input("Enter name of the Image: ")
    PROJECT_PATH = ""
    IMAGE_SOURCE_PATH = os.path.join(PROJECT_PATH, "data/processed/images")
    IMAGE_PATH = os.path.join(IMAGE_SOURCE_PATH, image_name)

    resize_and_export(IMAGE_PATH, IMAGE_SOURCE_PATH, 96, 96)
