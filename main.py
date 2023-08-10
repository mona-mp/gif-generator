import logging
from video_to_gif.validation import is_valid_video
from video_to_gif.video_tools import get_dimensions, get_fps, get_overlay_text

# Logging configuration

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

file_path = input("Enter the path to the video file: ")

# Validate the provided file path
if is_valid_video(file_path):
    logging.info("Valid video!")
    width, height = get_dimensions()
    fps = get_fps()
    text_content = get_overlay_text()
