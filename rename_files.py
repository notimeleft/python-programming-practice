#!/usr/bin/env python
from os import rename, listdir, getcwd




baseDir =getcwd()
desc = baseDir[baseDir.rfind('/')+1:]

fnames = listdir(baseDir)


for fname in fnames:    
    if(fname!="rename_files.py") and fname[0].isdigit and not fname[0].startswith("."):
    	
    	#print baseDir+"/"+fname, baseDir+"/"+fname[:3]+" "+desc+".jpg"
    	rename(baseDir+"/"+fname, baseDir+"/"+fname[:3]+" "+desc+".jpg")