from distutils.core import setup
from setuptools import find_packages

REQUIREMENTS = [
    'marvinbot',
    'requests'
]

setup(name='quote',
      version='0.1',
      description='Get random quotes of different categories',
      author='Jorge Dominguez',
      author_email='',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      package_data={'': ['*.ini']},
      install_requires=REQUIREMENTS,
      dependency_links=[
          'git+ssh://git@github.com:BotDevGroup/marvin.git#egg=marvinbot',
      ],)
