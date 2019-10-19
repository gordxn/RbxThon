import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rython",
    version="0.0.1",
    author="Gordxn",
    author_email="",
    description="Open-Source Roblox API built with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gordxn/Rython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)