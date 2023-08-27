import pytest
from contrastify import compute_contrast

def test_valid_contrast():
    color1 = (255, 255, 255)  # White
    color2 = (0, 0, 0)  # Black
    assert compute_contrast(color1, color2) == 21  # The contrast ratio for black and white is 21:1

def test_invalid_color_input():
    with pytest.raises(ValueError):
        compute_contrast((256, 255, 255), (0, 0, 0))
