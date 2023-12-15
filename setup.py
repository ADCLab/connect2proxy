import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "connect2proxy",
    version = "0.0.1",
    author = "Adan E Vela",
    author_email = "adan.vela@ucf.edu",
    description = ("Simple collection of code for connecting torguard proxies easier"),
    license = "Apache License 2.0",
    keywords = "proxy torguard",
    url = "https://github.com/ADCLab/connect2proxy",
    packages=['connect2proxy', 'testing'],
    install_requires=['pandas','pyyaml', 'requests'], #external packages as dependencies
    long_description=read('README.md'),
)