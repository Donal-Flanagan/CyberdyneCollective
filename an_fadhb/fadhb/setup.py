from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='diarmaidi2xpackage',
      version='0.1',
      description='The funniest joke in the world',
      long_description=readme(),
      url='https://github.com/Diemo-zz/I2X',
      author='Diarmaid de Búrca',
      author_email='diarmaiddeburca@gmail.com',
      license='MIT',
      packages=['diarmaidi2xpackage'],
      install_requires=[
          'nltk',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)