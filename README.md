# 🎨 Contrastify
![GitHub last commit](https://img.shields.io/github/last-commit/Ahmed-Jabrane/Contrastify)
![GitHub issues](https://img.shields.io/github/issues/Ahmed-Jabrane/Contrastify)
![GitHub contributors](https://img.shields.io/github/contributors/Ahmed-Jabrane/Contrastify)
![GitHub](https://img.shields.io/github/license/Ahmed-Jabrane/Contrastify)

A color contrast tool designed for designers, developers, and accessibility advocates.

## 📘 👁️‍🗨️ Why Good Contrast Matters

Contrastify is a tool built to facilitate color contrast checking, ensuring that designs are not only aesthetically pleasing but also accessible to all users, including those with visual impairments. 
Effortlessly verify if color combinations meet the [WCAG guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/).


## 📦 Installation

### 1.Clone the GitHub repository:
First, navigate to the directory where you want to clone the repository and run:

```bash
git clone https://github.com/Ahmed-Jabrane/Contrastify.git
```
### 2.Navigate to the cloned directory:

```bash
cd Contrastify
```

### 3.Install the package locally:
You can install the package in "editable" mode, which means changes to the source files will immediately affect the installed package:

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