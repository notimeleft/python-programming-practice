#!/usr/bin/env python
from os import rename, listdir


fnames = listdir('.')

for fname in fnames:    
    if(fname!="rename_files.py"):
    	rename(fname, fname[46:])