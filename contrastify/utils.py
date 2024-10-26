

def hex_to_rgb(hex_color):
    """
    Convert a HEX color string to an RGB tuple.

    Parameters:
    - hex_color: HEX color string (e.g., "#FFFFFF" or "FFFFFF").

    Returns:
    - Tuple of (R, G, B) values ranging from 0 to 255.
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def validate_rgb(color):
    """
    Validate if the given tuple represents a valid RGB color.

    Parameters:
    - color: Tuple of (R, G, B) values.

    Returns:
    - Boolean indicating if the tuple is a valid RGB color.
    """
    if not isinstance(color, tuple) or len(color) != 3:
        return False
    return all(0 <= value <= 255 for value in color)

def validate_hex(hex_color):
    """
    Validate if the given string represents a valid HEX color.

    Parameters:
    - hex_color: HEX color string.

    Returns:
    - Boolean indicating if the string is a valid HEX color.
    """
    if not isinstance(hex_color, str):
        return False
    hex_color = hex_color.lstrip('#')
    return len(hex_color) == 6 and all(c in '0123456789ABCDEFabcdef' for c in hex_color)

