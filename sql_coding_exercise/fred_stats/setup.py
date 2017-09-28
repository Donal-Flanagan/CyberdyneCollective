from distutils.core import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='fred_stats',
    version='0.1dev',
    description='short description',
    author='me',
 	author_email='me@myself.com',
 	# url='some_url',
    # packages=['fred_stats'],
    # install_requires=['other', 'packages'],  # external packages
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=long_description
)