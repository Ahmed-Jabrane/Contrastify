import pytest
from contrastify import check_wcag_norms

def test_wcag_checks():
    contrast_value = 7.5
    results = check_wcag_norms(contrast_value)
    
    assert results['AA'] == True
    assert results['AAA'] == True
