import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proxyauthenticator",
    version="0.0.1",
    author="Nuwan Chaminda",
    author_email="lokupodda123@gmail.com",
    description="Proxy Authenticator for python projects",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3.8.5",
        "License :: Boost Software License  Approved :: Boost License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)