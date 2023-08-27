# contrastify/wcag.py

def check_wcag_norms(contrast_ratio, text_size='normal'):
    """
    Check if a given contrast ratio meets WCAG norms.

    Parameters:
    - contrast_ratio: Float value representing the contrast ratio.
    - text_size: 'normal' or 'large'. WCAG has different requirements based on text size.

    Returns:
    - Dictionary with WCAG norms as keys and boolean values indicating if the contrast meets the norm.
    """
    norms = {
        'AA': 4.5,
        'AA Large': 3.0,
        'AAA': 7.0,
        'AAA Large': 4.5
    }

    if text_size == 'large':
        aa_required = norms['AA Large']
        aaa_required = norms['AAA Large']
    else:
        aa_required = norms['AA']
        aaa_required = norms['AAA']

    results = {
        'AA': contrast_ratio >= aa_required,
        'AAA': contrast_ratio >= aaa_required
    }

    return results

