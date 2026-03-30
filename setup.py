from setuptools import setup

setup(
    name="colourful-fortune",
    version="0.1.0",
    py_modules=["colourful_fortune"],
    install_requires=[
        "lol-cat-py",
    ],
    entry_points={
        "console_scripts": [
            "colourful-fortune=colourful_fortune:main",
        ],
    },
    author="Your Name",
    description="Run `fortune` and print the output in rainbow colors with lol-cat-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
)
