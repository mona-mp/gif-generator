# validation.py inside the video_to_gif package

import logging
import os
import subprocess

import ffmpeg

# Validates if the given path points to a valid video file.


def is_valid_video(file_path):

    # 1. Check if file exists
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return False

    # 2. Check file extension (basic validation)
    valid_extensions = ['.mp4', '.avi', '.mkv', '.flv', '.mov']
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in valid_extensions:
        logging.error(f"Invalid file extension: {ext}")
        return False

    # 3. Use FFmpeg to validate video content
    try:
        probe = ffmpeg.probe(file_path)

        # You can add additional validation here based on the probe result if needed
        return True
    except ffmpeg.Error as e:
        logging.error(f"Error checking video: {e}")
        return False
