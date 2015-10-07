"""
Setup script so this package can be installed using distutils, setuptools, or pip
"""

from setuptools import setup

setup(
    name="gaedeployer",
    version="1.0",
    description="Huge Library for deploying python projects to GAE.",
    py_modules=['gaedeployer', 'observer', 'deployer'],
    entry_points={
        'console_scripts': [
            'gaedeployer=gaedeployer:main',
        ],
    },
)
