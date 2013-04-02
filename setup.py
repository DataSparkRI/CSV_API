try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An api for csv files',
    'author': 'Provplan Devops',
    'url': '',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['pymongo'],
    'packages': [''],
    'scripts': [],
    'name': 'csv_api'
}

setup(**config)
