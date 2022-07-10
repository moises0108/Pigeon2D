from setuptools import setup

setup(name='Pigeon2D',
      version='1.2',
      description='A game engine for python pygame.',
      url='https://github.com/desvasicek/Pigeon2D',
      author='desvasicek',
      author_email=None,
      license='MIT',
      packages=[],
      install_requires="pygame>=1.9.6",
      zip_safe=False,
      setup_requires=['pytest-runner'],
      long_description=open("index.rst").read(),
      tests_require=['pytest'],
      classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Topic :: Games/Entertainment",
        "Natural Language :: English",
        "Intended Audience :: Developers"
      ])
