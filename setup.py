import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="memchess",
    version="1.0.0",
    author="Tibor Reiss",
    author_email="tibor.reiss@gmail.com",
    description="Memsource chess homework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tibor-reiss/memchess",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'flask',
        'pytest-mock'
    ],
    python_requires='>=3.8',
)
