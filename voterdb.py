#! /usr/bin/env python

import sqlite3, os, urllib

def writeDB():
	conn = sqlite3.connect('example.db')
	c = conn.cursor()

	c.execute('''CREATE TABLE IF NOT EXISTS twitter_users
		     (date text, whatever real)''')

	c.execute("INSERT INTO twitter_users VALUES ('2005-05-05',12.23)")

	conn.commit()
	conn.close()

def downloadData():
	directory = "datadir"
	ncboeDir = "ftp://alt.ncsbe.gov/data/ncvoter68.zip"

	if not os.path.exists(directory):
		os.makedirs(directory)
	os.chdir(directory)
	urllib.urlretrieve(ncboeDir, 'ncvoter68.zip')

downloadData()
