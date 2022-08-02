""" AIID provides weekly snapshots of their database in tar.bz2
Use this program to easily extract the database file into spreadsheets

Just replade the NAME variable with the name/path of the tar.bz2 file 
downloaded from the AIID website.

EXAMPLE: NAME = 'database.tar.bz2'

A new folder named mongodump will be created in your current directory

Link to AIID snapshots: https://incidentdatabase.ai/research/snapshots"""

import tarfile

NAME = 'backup-20220801102740.tar.bz2'

x=""
tar = tarfile.open(NAME)  
tar.extractall(x)
print(x)
tar.close()