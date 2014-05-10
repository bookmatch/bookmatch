from setuptools import setup


requires = [
    "pyramid",
    "pyramid_mako",
    "pyramid_tm",
    "pyramid_layout",
]


setup(name="bookmatch",
      install_requires=requires,
      packages=['bookmatch'],
      include_package_data=True,
)
