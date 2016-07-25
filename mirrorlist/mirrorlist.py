#!/usr/bin/env python

import os
import json


def test_file(filename, mode='r'):
	try:
		with open(filename, mode) as f:
			pass

	except OSError:
		return False

	return True


def replace_mirrors(oldpath, newpath, country):
	with open(oldpath, 'w') as old, open(newpath, 'r') as new:
		german = False

		for line in new:
			if ''.join(line.split()).startswith('##{}'.format(country)):
				german = True
			elif german and ''.join(line.split()).startswith('##'):
				german = False

			if german and line.startswith('#Server') and line.find('https') > -1:
				print(line.lstrip('#'), end='', file=old)
			else:
				print(line, end='', file=old)

	os.remove(newpath)


if __name__ == '__main__':
	old = '/etc/pacman.d/mirrorlist'
	new = '/etc/pacman.d/mirrorlist.pacnew'
	country = 'Germany'

	with open('/etc/mirrorlist-selector.json') as f:
		conf = json.load(f)
		old = conf['mirrorlist_old']
		new = conf['mirrorlist_new']
		country = conf['contry']

	if test_file(OLD, 'w') and test_file(NEW, 'r'):
		replace_mirrors(OLD, NEW, COUNTRY)
