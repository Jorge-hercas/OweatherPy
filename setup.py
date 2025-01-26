

from setuptools import setup, find_packages

setup(
    name="OweatherPy",
    version="0.1.0",
    author="Tu Nombre",
    author_email="tuemail@example.com",
    description="A Python library for interacting with OpenWeather API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)