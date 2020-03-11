import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mjjuszczak", # Replace with your own username
    version="0.0.1",
    author="Matthew Juszczak",
    author_email="mjuszczak@uchicago.edu",
    description="MSCA Class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mjjuszczak/Python_for_Analytics_Assignment_3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)