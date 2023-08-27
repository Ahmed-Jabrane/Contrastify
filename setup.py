from setuptools import setup, find_packages

setup(
    name='contrastify',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # any dependencies your package might have
    ],
    author='Your Name',
    author_email='its.jabrane.ahmed@gmail.com',
    description='A color contrast tool designed for designers, developers and accessibility advocates.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',  # or any other license you choose
    keywords='contrast color wcag',
    url='https://github.com/Ahmed-Jabrane/Contrastify',  # link to the GitHub repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
