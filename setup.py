from setuptools import setup, find_packages

setup(name='PyExZ3',
      version='0.1',
      description='Python Exploration with Z3',
      url='http://github.com/uds-se/PyExZ3',
      author='Thomas J Ball',
      author_email='',
      license='https://github.com/uds-se/PyExZ3/blob/master/copyright.txt',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      install_requires=[],
      zip_safe=False)
