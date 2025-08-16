# setup.py
from setuptools import setup, find_packages

setup(
    name="EmotionDetection",          # package name shown to pip
    version="0.1.0",
    description="Simple emotion detection package (HuggingFace based)",
    author="Your Name",
    packages=find_packages(),         # will include the EmotionDetection package
    include_package_data=True,
    install_requires=[
        "requests>=2.25"
    ],
    python_requires=">=3.8",
)
