import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="micropython-wifi-tool",
    version="0.0.1",
    author="shilin cai",
    author_email="caishilin@yahoo.com",
    description="A wifi tool for micropython",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SSBun/micropython-wifi-tool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)