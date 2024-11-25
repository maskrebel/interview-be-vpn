import setuptools


version = "0.0.1"

setuptools.setup(
    name="custom_hash",
    version=setuptools.sic(version),
    author="wardi.fadillah",
    author_email="wardi.fadillah@gmail.com",
    description="custom_hash",
    long_description="custom_hash",
    long_description_content_type="text/markdown",
    url="",
    install_requires=['Django==3.2.13'],
    packages=setuptools.find_packages(include=['custom_hash', 'custom_hash.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
