import logging

import ffmpeg


def get_dimensions():
    while True:  # Loop until a valid input is provided
        dimensions = input(
            "Enter desired dimensions (width x height, e.g., 1280x720): ")
        try:
            width, height = map(int, dimensions.split('x'))
            return width, height
        except ValueError:
            logging.error(
                f"Invalid dimensions: {dimensions}. Please use the format width x height, e.g., 1280x720.")


def get_fps():
    while True:  # Loop until a valid input is provided
        fps_input = input("Enter desired frame rate (FPS) for the GIF: ")
        try:
            fps = int(fps_input)
            if fps <= 0:
                raise ValueError("FPS should be a positive integer.")
            return fps
        except ValueError:
            logging.error(
                f"Invalid FPS value: {fps_input}. Please enter a positive integer.")


def get_overlay_text():
    while True:  # Loop until a valid input is provided
        answer = input(
            "Would you like to overlay text on the GIF? (yes/no): ").lower()
        if answer == 'yes':
            text = input("Please enter the text you'd like to overlay: ")
            if text:
                return True, text
            logging.error("Text cannot be empty. Please enter a valid text.")
        elif answer == 'no':
            return False, None
        else:
            logging.error("Invalid choice. Please enter 'yes' or 'no'.")


def extract_video_segment(input_path, start_time, duration, output_path):
    try:
        (
            ffmpeg
            .input(input_path, ss=start_time, t=duration)
            .output(output_path, c='copy')
            .run()
        )
    except ffmpeg.Error as e:
        logging.error(f"Error while extracting segment: {e}")


def adjust_video(input_path, width, height, fps, output_path):
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, vf=f'scale={width}:{height}', r=fps)
            .run()
        )
    except ffmpeg.Error as e:
        logging.error(f"Error adjusting video: {e}")


def overlay_text(input_path, text, position, output_path):
    # Positions can be 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'center'
    position_mappings = {
        'top-left': '(10,10)',
        'top-right': '(main_w-text_w-10,10)',
        'bottom-left': '(10,main_h-text_h-10)',
        'bottom-right': '(main_w-text_w-10,main_h-text_h-10)',
        'center': '(main_w/2-text_w/2,main_h/2-text_h/2)'
    }

    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, vf=f'drawtext=text={text}:x={position_mappings[position]}:y={position_mappings[position]}:fontsize=24:fontcolor=white')
            .run()
        )
    except ffmpeg.Error as e:
        logging.error(f"Error overlaying text: {e}")


def convert_to_gif(input_path, output_path):
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, f='gif')
            .run()
        )
    except ffmpeg.Error as e:
        logging.error(f"Error converting to GIF: {e}")
