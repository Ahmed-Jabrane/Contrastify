
from contrastify.utils import validate_rgb


def compute_contrast(color1, color2):
    """
    Compute the contrast ratio between two colors.

    Parameters:
    - color1: Tuple of (R, G, B) values ranging from 0 to 255.
    - color2: Tuple of (R, G, B) values ranging from 0 to 255.

    Returns:
    - Contrast ratio as a float.
    """

    if not validate_rgb(color1) or not validate_rgb(color2):
        raise ValueError("Invalid RGB values provided.")
    
    luminance1 = _get_relative_luminance(color1)
    luminance2 = _get_relative_luminance(color2)

    L1, L2 = max(luminance1, luminance2), min(luminance1, luminance2)

    return (L1 + 0.05) / (L2 + 0.05)

def _get_relative_luminance(color):
    """
    Calculate the relative luminance of a color.

    Parameters:
    - color: Tuple of (R, G, B) values ranging from 0 to 255.

    Returns:
    - Relative luminance as a float.
    """
    r, g, b = [x / 255.0 for x in color]  

    r = _gamma_correct(r)
    g = _gamma_correct(g)
    b = _gamma_correct(b)

    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return luminance

def _gamma_correct(channel_value):
    """
    Gamma correction for sRGB values.

    Parameters:
    - channel_value: Float value of an RGB channel, normalized to [0, 1].

    Returns:
    - Gamma-corrected value as a float.
    """
    if channel_value <= 0.03928:
        return channel_value / 12.92
    else:
        return ((channel_value + 0.055) / 1.055) ** 2.4
