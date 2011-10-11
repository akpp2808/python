import sys
from setuptools import setup

version = '0.9'

tests_require = ['nose', 'dnspython']

setup(name="fv_email",
      version=version,
      description="Improved FormEncode e-mail validation",
      long_description="""\
Improves on the formencode email validator by using dnspython rather than pydns
for resolving tests, handling idna/unicode domains as well as protecting
against additional user errors.
""",
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: Python Software Foundation License",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
      author="Joseph Tate",
      author_email="joseph.tate@palemountain.com",
      url="http://bitbucket.org/josephtate/formencode-email/",
      license="PSF",
      zip_safe=False,
      provides=['fv_email'],
      install_requires=[
        "formencode",
      ],
      packages=["fv_email"],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=tests_require
      )
