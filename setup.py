try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Download the information for top 100 cryptocurrencies and save them to csv',
    'author': 'Rajiv Galva',
    'author_email': 'rajiv.galva@uoit.net',
    'version': '0.0.1',
    'packages': find_packages(),
    'name': 'cryptoinfo'
}

setup(**config)