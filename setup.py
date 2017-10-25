#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from setuptools import find_packages, setup
import sysconfig

NAME = 'rackattack-api'
DESCRIPTION = 'Rackattack API repo'
URL = 'https://github.com/stratoscale/rackattack-api'
EMAIL = 'ruslan.portnoy@stratoscale.com'
AUTHOR = 'Stratoscale'
PKG_INFO = 'PKG-INFO'
REQUIRED = []


def _get_version_hash():
    """get from git the tag/hash of our latest commit"""
    try:
        proc = subprocess.Popen(["git", "describe", "--tags", "--dirty", "--always"], stdout=subprocess.PIPE)
    except EnvironmentError:
        print("Couldn't run git to get a version number for setup.py")
        return "N/A"
    ver = proc.communicate()[0]
    return ver.strip()


def version():
    if os.path.exists(PKG_INFO):
        with open(PKG_INFO) as package_info:
            for key, value in (line.split(':', 1) for line in package_info):
                if key.startswith('Version'):
                    return value.strip()

    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()


here = os.path.abspath(os.path.dirname(__file__))
_version = version()
_packages = find_packages('py')  # , exclude=('test',))
print(_packages)

# site_packages_path_pure = sysconfig.get_path('purelib')
# site_packages_path_plat = sysconfig.get_path('platlib')
data_files = [
    # (site_packages_path_pure, ["rackattack-api.pth"]),
    # ('', ["rackattack-api.pth"]),
    # (site_packages_path_plat, ["rackattack-api.pth"]),
    (os.path.join(sys.prefix, 'lib/python%s/site-packages' % sys.version[:3]), ["rackattack-api.pth"]),
]

# from distutils import sysconfig
# site_packages_path = sysconfig.get_python_lib()
# data_files.append((site_packages_path, ["rackattack-api.pth"]))


setup(
    name=NAME,
    version=_version,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=_packages,
    package_dir={
        'rackattack': 'py/rackattack',
    },
    data_files=data_files,
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[  # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
