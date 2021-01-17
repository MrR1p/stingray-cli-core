from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="stingray_cli_core",
    version='2.1.1',
    author="Stingray Technologies LLC",
    description="Stingray core package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Swordfish-Security/stingray-cli-core",
    packages=find_packages(),
    author_email='stingray@appsec.global',
    include_package_data=True,
    install_requires=[
         'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
)
