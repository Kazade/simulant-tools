import os
from setuptools import setup, find_packages


NAME = 'simulant-tools'
PACKAGES = find_packages()
DESCRIPTION = 'Tools to harness the Simulant Game Engine'
URL = "https://simulant-engine.appspot.com/"
LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
AUTHOR = 'Luke Benstead'
VERSION = '0.1a0'

setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    scripts=['simulant'],
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=["gamedev", "game", "engine", "simulant"],
    url=URL,
    install_requires=[
        'docker'
    ],
    classifiers=[
        'Environment :: Console'
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
    ],
    include_package_data=True,
    data_files=[
        ('share/simulant/template/assets', ['template/assets/README']),
        ('share/simulant/toolchains', ['toolchains/Dreamcast.cmake']),
        ('share/simulant/toolchains', ['toolchains/IP.TMPL']),
        ('share/simulant/template/libraries', ['template/libraries/README']),
        ('share/simulant/template/sources', ['template/sources/main.cpp']),
        ('share/simulant/template/sources/scenes', ['template/sources/scenes/game.cpp']),
        ('share/simulant/template/sources/scenes', ['template/sources/scenes/game.h']),
        ('share/simulant/template/', ['template/CMakeLists.txt']),
        ('share/simulant/template/', ['template/simulant.json']),
    ]
)
