import logging
from video_to_gif.validation import is_valid_video

# Logging configuration

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

file_path = input("Enter the path to the video file: ")

# Validate the provided file path
if is_valid_video(file_path):
    logging.info("Valid video!")
