# 🎨 Contrastify
![GitHub last commit](https://img.shields.io/github/last-commit/Ahmed-Jabrane/Contrastify)
![License](https://img.shields.io/badge/license-MIT-green)
![Python version](https://img.shields.io/badge/python-3.8%2B-blue)


## 👁️‍🗨️ Why Good Contrast Matters

Contrastify is a tool built to facilitate color contrast checking, ensuring that designs are not only aesthetically pleasing but also accessible to all users ([WCAG guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/)), including those with visual impairments.


## 📦 Installation

### 1.Clone the repository:

```bash
git clone https://github.com/Ahmed-Jabrane/Contrastify.git
```
### 2.Navigate to the cloned directory:

```bash
cd Contrastify
```

### 3.Install the package locally:
```bash
pip install -e .
```

## 🛠️ Usage

### Compute Contrast Ratio
```python
from contrastify import compute_contrast, check_wcag_norms
from contrastify.utils import hex_to_rgb

color1 = hex_to_rgb("#FFFFFF")  # White
color2 = hex_to_rgb("#000000")  # Black

contrast_ratio = compute_contrast(color1, color2)
print(f"Contrast Ratio: {contrast_ratio:.2f}")

```

### Check Against WCAG Norms
```python
wcag_results = check_wcag_norms(contrast_ratio)

for norm, meets_criteria in wcag_results.items():
    status = "meets" if meets_criteria else "does not meet"
    print(f"The contrast ratio {status} the {norm} criteria.")

```

## 🤝 Contributing

Guidelines for contributing to "Contrastify". Direct readers to `CONTRIBUTING.md` for detailed instructions.

## 📄 License

Contrastify is under the MIT License. See `LICENSE` file for more details.

## 📚 Further Reading
To understand more about the importance of color contrast and accessibility guidelines, refer to the following resources:
The WCAG guidelines provide extensive recommendations for making web content more accessible. These guidelines are used globally and form the basis for many regional accessibility laws and policies. ([Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/))
