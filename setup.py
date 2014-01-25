from setuptools import setup, find_packages
import os

here = os.path.dirname(__file__)


requires = [
    "pyramid>=1.5dev",
    "sqlalchemy>=0.9",
    "zope.sqlalchemy",
    "deform>=2.0dev",
    "pyramid_tm",
    "pyramid_mako",
    "pyramid_layout",
    "pyramid_deform",
    "pillow",
]


tests_require = [
    "testfixtures",
    "webtest",
]

def _read(name):
    try:
        with open(os.path.join(here, name)) as f:
            return f.read()
    except:
        return ""


readme = _read("README.rst")

setup(name="bookmatch",
      long_description=readme,
      install_requires=requires,
      packages=find_packages(),
      test_suite="bookmatch",
      extras_require={
          "testing": tests_require,
          "dev": tests_require + ["waitress", "pyramid_debugtoolbar"],
      }
      )