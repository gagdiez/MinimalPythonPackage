''' Setup file '''
from os import path

from setuptools import setup
import numpy

package_name = 'phds'

cli_module = package_name + '.cli'

setup(name=package_name,
      version='1',
      description='Example of packaging in python',
      url='http://github.com/gagdiez/phds',
      author='Gallardo Diez, Guillermo Alejandro',
      author_email='guillermo-gallardo.diez@inria.fr',
      include_package_data=True,
      packages=[package_name, cli_module],
      scripts=['scripts/word_count', 'scripts/flip_text'])
