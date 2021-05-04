from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Script that sort your scrappy files',
      author='Garmr',
      author_email='nvova@i.ua',
      license='MIT',
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']},
      packages=find_namespace_packages())