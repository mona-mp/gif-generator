import logging
import ffmpeg

# Resizing


def get_dimensions():
    try:
        width, height = map(int, input(
            "Enter desired output dimensions (width x height, e.g., 1280x720): ").split('x'))
        return width, height
    except ValueError:
        logging.error(
            "Invalid dimensions provided. Please use the format: widthxheight.")
        return None, None

# Frame rate


def get_fps():
    try:
        fps = int(input("Enter the desired frame rate (e.g., 24 for 24 FPS): "))
        return fps
    except ValueError:
        logging.error(
            "Invalid frame rate provided. Please enter an integer value.")
        return None

# Overlay Text


def get_overlay_text():
    try:
        add_text = input("Do you want to add text overlay? (yes/no): ").lower()
        if add_text == 'yes':
            text_content = input("Enter the text to overlay: ")
            return text_content
        return None
    except Exception as e:
        logging.error(f"Error getting overlay text: {e}")
        return None
