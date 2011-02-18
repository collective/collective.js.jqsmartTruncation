from setuptools import setup, find_packages
import os

version = open('collective/js/jqsmartTruncation/version.txt').read().strip()
maintainer = 'Elio Schmutz'

setup(name='collective.js.jqsmartTruncation',
      version=version,
      description="truncate too long text",
      long_description=open("README.txt").read() + "\n" +
                    open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='jquery smartTruncation',
      author='%s, 4teamwork GmbH' % maintainer,
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      license='GPL2',
      url='http://plugins.jquery.com/project/smarttruncation',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
