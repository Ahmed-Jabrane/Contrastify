from setuptools import setup, find_packages

setup(
    name='contrastify',
    version='0.1',
    packages=find_packages(),
    author='Ahmed Jabrane',
    author_email='its.jabrane.ahmed@gmail.com',
    description='A color contrast tool designed for designers, developers and accessibility advocates.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',  
    keywords='contrast color wcag',
    url='https://github.com/Ahmed-Jabrane/Contrastify',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
