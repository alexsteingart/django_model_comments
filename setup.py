#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django_model_comments',
    version='1.0',
    description="",
    author="twig",
    author_email='alex@pickipicki.com',
    url='',
    packages=find_packages(),
    package_data={
	'django_model_comments': [
			'templates/*.*',
			'templates/*/*.*,
			'templates/*/*/*.*,
			'templates/*/*/*/*.*,

			],
	},
)

