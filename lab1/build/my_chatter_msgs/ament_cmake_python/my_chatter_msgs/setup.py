from setuptools import find_packages
from setuptools import setup

setup(
    name='my_chatter_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('my_chatter_msgs', 'my_chatter_msgs.*')),
)
