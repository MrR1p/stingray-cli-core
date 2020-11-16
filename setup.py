import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stingray_core",
    version=os.getenv("VERSION", "dev"),
    author="AppSec Solutions",
    description="Stingray core package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/appsec-audit/stingray",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
    #     'mitmproxy==4.0.4',
    #     'pymysql==0.8.0',
    #     'protobuf==3.5.2.post1',
    #     'xmltodict==0.11.0',
    #     'psutil==5.4.3',
    #     'pandas==0.22.0',
    #     'tablib==0.12.1',
    #     'bcrypt==3.1.4',
    #     'click==6.7',
    #     'python-magic==0.4.15',
    #     'pyjks==17.1.1',
    #     'PyJWT==1.7.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
)
