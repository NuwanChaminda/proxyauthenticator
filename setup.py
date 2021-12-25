from setuptools import setup
from setuptools import find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="proxyauthenticator",
    version="0.0.1",
    author="Nuwan Chaminda",
    author_email="lokupodda123@gmail.com",
    description="Proxy Authenticator for python projects",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/NuwanChaminda/proxyauthenticator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT Software License  Approved :: MIT License",
        "Operating System :: OS Independent",
        # Programming Languages Used..
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    # package_dir={"": "src"},
    # Specify folder content.
    packages=find_namespace_packages(
        include=['src']
    ),
    python_requires=">=3.6",

)
