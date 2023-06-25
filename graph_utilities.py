import os
import shutil


def display_sentiment_score(sentiment_polarity):


    # Get terminal width and subtract 14 for padding on each side
    bar_width = (get_terminal_width() - 14)

    # Scale value to fit the bar width
    scaled_value = int((sentiment_polarity + 1) / 2 * bar_width)

    # Build bar string using Unicode characters
    bar = '|' + '█' * scaled_value + '░' * (bar_width - scaled_value) + '|'

    print(f"Sentiment Polarity: {sentiment_polarity:.4f}")
    print(f"{-1 :<5} {bar} {1 :>5}")


def get_terminal_width():
    """
    Get the width of the terminal in characters.

    The function first attempts to retrieve the terminal size using the `os` module.
    If this fails (for instance, if the code is not being run in a terminal), it falls
    back to using the `shutil` module, with a fallback size of 80x24.

    Returns:
        int: The width of the terminal in characters. If the width can't be determined, it returns 80.
    """

    try:
        # Try to get the size using the os module
        columns, _ = os.get_terminal_size(0)

    except OSError:

        # If that fails, use the shutil module and also provide a fallback
        columns = shutil.get_terminal_size(fallback=(80, 24)).columns

    return columns
