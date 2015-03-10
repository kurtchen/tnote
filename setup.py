#!/usr/bin/env python
#
#       setup.py
#       

from distutils.core import setup

setup(name = "tnote",
    version = "0.2.1",
    description = "sticky style notes for the terminal",
    author = "Ben Holroyd",
    author_email = "holroyd.ben@gmail.com",
    licence = "GPL v3+",
    scripts = ['tnote'],
    data_files = [('share/doc/tnote',['README','AUTHORS','COPYING','Changelog']),('share/man/man1',['tnote.1.gz'])]     
) 
