import logging


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
