# ColorCycler Algorithms
# Copyright © 2016  Dave Hocker (email: AtHomeX10@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the LICENSE file for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program (the LICENSE file).  If not, see <http://www.gnu.org/licenses/>.
#
# To build the package
# python setup.py build
#
# To install the package in the current venv
# python setup.py install
#
# To build a source distribution:
# python setup.py sdist
#
# To install distribution in current venv:
#   pip install -U dist/colorcycler-x.y.z.tar.gz
# where x.y.z is the version number (e.g. 1.0.0)
#

import os
import sys
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


def write_version(version):
    """
    Update the version file
    :param version: major.minor.build
    :return: None
    """
    f = open("version.txt", "w")
    f.write(version)
    f.close()
    print("Updated version:", version)


# Update the version build number on builds
# major.minor.build
if "build" in sys.argv:
    vt = read("version.txt")
    vlist = vt.split('.')
    vlist[2] = str(int(vlist[2]) + 1)
    write_version('.'.join(vlist))

setup(
    name='colorcycler',
    version=read("version.txt"),
    description='Color generation algorithms',
    long_description=(read('Readme.md')),
    url='www.github.com/dhocker/colorcycler',
    license='GPLv3. See LICENSE file.',
    author='Dave Hocker',
    author_email='AtHomeX10@gmail.com',
    py_modules=[],
    include_package_data=True,
    packages=find_packages(exclude=['tests*']),
    install_requires=[]
)