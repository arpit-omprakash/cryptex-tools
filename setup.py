import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cipherx", # Name of the package
    version="0.0.1",
    author="Arpit Omprakash",
    author_email="omprakasharpit@gmail.com",
    license='MIT',
    description="A simple package to encrypt and decrypt files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="", # Add project url
    packages=setuptools.find_packages(),
    classifiers=[
        # How mature the project is
        # 1 - Planning
        # 2 - Pre-Alpha
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        # 6 - Mature
        # 7 - Inactive
        "Development Status :: 1 - Planning"
        "Topic :: Cryptography :: Cipher Tools"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='cryptography cipher codec',
    python_requires='~=3.6',
)

## Notes for versioning:
# Given a version number MAJOR.MINOR.PATCH, increment the:
# MAJOR version when you make incompatible API changes,
# MINOR version when you add functionality in a backwards compatible manner, and
# PATCH version when you make backwards compatible bug fixes.
