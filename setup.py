from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read

setup(
    name='django-jsonforms',
    version='0.5',
    description='JSON Schema forms for Django',
    url='https://github.com/Aristotle-Metadata-Enterprises/django-jsonforms',
    author='Harry White',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['jsonfield','jsonschema','django']
)