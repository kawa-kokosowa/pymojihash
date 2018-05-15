from setuptools import setup
import ast

from pymojihash import __version__


with open('pymojihash/pymojihash.py') as f:
    module = ast.parse(f.read())
    readme_docstring = ast.get_docstring(module)

setup(
    name='pymojihash',
    version=__version__,
    include_package_data=True,
    description='Python 3 package for hashing strings to emojis.',
    long_description=readme_docstring,
    author='Lily FYI',
    author_email='hello@lily.fyi',
    packages=['pymojihash',],
    package_dir={'pymojihash': 'pymojihash',},
)
