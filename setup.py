import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="web3-input-decoder",
    version="0.3.0",
    author="VvWkQkTKJ",
    author_email="VvWkQkTKJ@protonmail.ch",
    description="FORK: web3-input-decoder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/r4VP4/web3-input-decoder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'web3>=6.0.0b9', 'pyinstrument', 'base58', 'ipfshttpclient'
    ],
    python_requires='>=3.9',
)
