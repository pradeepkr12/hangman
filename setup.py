#!/usr/bin/env python

from setuptools import setup

setup(name='Hangman',
      version='0.1.0',
      description=("The word game Hangman based on 'Invent Your "
                   "Own Computer Games with Python'."),
      author='Vijay Kumar B.',
      author_email='vijaykumar@bravegnu.org',
      url='http://github.com/chennaipy/hangman',
      scripts=['hangman.py'],
      install_requires=[
          'six',
      ],
      tests_require=[
          'unittest2',
          'mock',
      ],
      test_suite="test"
      )
