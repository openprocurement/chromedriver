from setuptools import setup, find_packages
import sys, os
from os.path import join
import imp

here = os.path.abspath(os.path.dirname(__file__))

setupy_download_helper_path = join(here, 'setupy_download_helper.py')
setupy_download_helper = imp.load_source(
    'setupy_download_helper', setupy_download_helper_path)

version = '2.21.1'
setupy_download_helper.CHROMEDRIVER_VERSION = version[:4]

with open(os.path.join(here, 'README.rst')) as fd:
    readme = fd.read()

setup(name='chromedriver',
      version=version,
      description='Tool for downloading chromedriver',
      long_description=readme,
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet :: WWW/HTTP :: Browsers',
          'Topic :: Software Development :: Testing',
      ],
      keywords='chromedriver',
      author='Maksym Shalenyi (enkidulan)',
      author_email='supamaxy@gmail.com',
      url='https://github.com/enkidulan/chromedriver',
      license='Apache License 2.0',

      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      py_modules=['setupy_download_helper'],
      include_package_data=True,
      zip_safe=False,
      cmdclass={
          'bdist_egg': setupy_download_helper.BdistEggCommand,
          'develop': setupy_download_helper.DevelopCommand,
          'install': setupy_download_helper.InstallCommand,
      },
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      package_data={'chromedriver': ['bin/chromedriver']},
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
