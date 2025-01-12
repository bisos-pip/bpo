#!/usr/bin/env python

# Template File:  "/bisos/apps/defaults/begin/templates/purposed/pyModule/python/setup.py"

####+BEGIN: bx:dblock:global:file-insert :mode python :file "/bisos/apps/defaults/begin/templates/purposed/pyModule/python/commonSetupCode.py"

import setuptools
import re
import inspect
import pathlib

def pkgName():
    """ From this eg., filepath=.../bisos-pip/PkgName/py3/setup.py, extract PkgName. """
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    grandMother = pathlib.Path(filename).resolve().parent.parent.name
    return f"bisos.{grandMother}"

def description():
    """ Extract title from ./README.org which is expected to have a title: line. """
    try:
        with open('./README.org') as file:
            while line := file.readline():
                if match := re.search(r'^#\+title: (.*)',  line.rstrip()):
                    return match.group(1)
                return "MISSING TITLE in ./README.org"
    except IOError:
        return  "ERROR: Could not read ./README.org file."

def longDescription():
    """ Convert README.org to README.rst. """
    try:
        import pypandoc
    except ImportError:
        result = "WARNING: pypandoc module not found, could not convert to RST"
        return result
    if (result := pypandoc.convert_file('README.org', 'rst')) is None:
        result = "ERROR: pypandoc.convert_file('README.org', 'rst') Failed."
    return result

####+END:

# :curDevVer "0.92" :pypiNextVer "0.95"
####+BEGIN: b:py3:pypi/nextVersion :increment 0.01

# ./pypiUploadVer does not exist -- pypiNextVer=0.41 -- installedVersion=0.5
def pkgVersion():
        return '0.5'  # Version Nu Of Installed Pkg

####+END:

####+BEGIN: b:py3:pypi/requires :extras ()

requires = [ 
"blee",
"blee.icmPlayer",
"bisos",
"bisos.b",
"bisos.basics",
"bisos.common",
"bisos.crypt",
"bisos.currents",
"bisos.icm",
"bisos.pals",
"from",
]
####+END:

####+BEGIN: b:py3:pypi/scripts :comment ""

scripts = [ 
'./bin/bpoManage.cs',
'./bin/bpoRepos.cs',
]
####+END:

#
# Data files would be  specified in ./MANIFEST.in as: # recursive-include bisos/pkgName *
#

data_files = [
]

# :pkgName "--auto--"  --- results in use of name=pkgName(),
####+BEGIN: b:py3:pypi/setupFuncArgs :pkgName ""

setuptools.setup(
    name='bisos.bpo',
    version=pkgVersion(),
    packages=setuptools.find_packages(),
    scripts=scripts,
    #data_files=data_files,
    include_package_data=True,
    zip_safe=False,
    author='Mohsen Banan',
    author_email='libre@mohsen.1.banan.byname.net',
    maintainer='Mohsen Banan',
    maintainer_email='libre@mohsen.1.banan.byname.net',
    url='http://www.by-star.net/PLPC/180047',
    license='AGPL',
    description=description(),
    long_description=longDescription(),
    download_url='http://www.by-star.net/PLPC/180047',
    install_requires=requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )

####+END:
