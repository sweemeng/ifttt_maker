from setuptools import setup

setup(name='ifttt_maker',
      version='0.0.1',
      description='A simple interface to ifttt maker',
      url='http://github.com/sweemeng/ifttt_maker',
      author='sweemeng',
      author_email='sweester@gmail.com',
      license='BSD',
      packages=['ifttt_maker'],
      install_requires=[
          'requests',
      ],
      test_suite="tests",
      zip_safe=False)
