import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bsrp",
    version="1.0",
    author="Abe Hoffman",
    author_email="abehoffman@me.com",
    license='MIT',
    description="B-first SRP-6a protocol implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abehoffman/bsrp",
    install_requires=[],
    tests_require=[
        "pytest",
        "pytest-cov",
    ],
    packages=setuptools.find_namespace_packages("lib"),
    package_dir={"": "lib"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)