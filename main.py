import logging
from video_to_gif.validation import is_valid_video
from video_to_gif.video_tools import adjust_video, convert_to_gif, extract_video_segment, get_dimensions, get_fps, get_overlay_text, overlay_text

# Logging configuration

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

file_path = input("Enter the path to the video file: ")

# Validate the provided file path
if is_valid_video(file_path):
    logging.info("Valid video!")

# Get gif start time and duration from video
start_time = float(input("Enter start time of the segment (in seconds): "))
duration = float(input("Enter duration of the segment (in seconds): "))

output_segment_path = "temp_segment.mp4"

extract_video_segment(file_path, start_time, duration, output_segment_path)

# Get dimensions
width, height = get_dimensions()

# Get fps
fps = get_fps()

# Adjust video dimensions and FPS
adjusted_video_path = "temp_adjusted.mp4"
adjust_video(output_segment_path, width, height, fps, adjusted_video_path)

#  Addoverlay text on the video
overlay, text = get_overlay_text()

if overlay:
    # Get the position for the overlay from the user
    valid_positions = ['top-left', 'top-right',
                       'bottom-left', 'bottom-right', 'center']
    position = ''
    while position not in valid_positions:
        position = input(
            "Enter text position (top-left, top-right, bottom-left, bottom-right, center): ").strip().lower()
        if position not in valid_positions:
            logging.error(
                f"Invalid position: {position}. Please select from the given choices.")
    overlay_text(adjusted_video_path, text, position, adjusted_video_path)

# Convert to GIF
output_gif_path = "output.gif"
convert_to_gif(adjusted_video_path, output_gif_path)
